from util import suppress
suppress.all()
#suppress.langchain_warnings()
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from crewai import Crew
from agents import load_default_agent
from src.banner import print_banner
from datetime import datetime
from src import vectorstore
import os
import json

os.makedirs("/tmp/agents", exist_ok=True)
os.makedirs("/tmp/rag", exist_ok=True)

app = FastAPI()

# Enable CORS for frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://truenotionai.github.io/"], # Change to "*" during development and replace with your frontend domain after deployment 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Initializing..")
print_banner()

# Global variables for conversation, retriever and crew instance
chat_history = []  # Each element is a tuple (user query, AI answer)
history_mode = True
crew_instance = None
retriever = None
loaded_files_reference = []
disable_agent= False
k = None
chunk_size = None
memory = None  # Number of historical conversation pairs to include

try:
    with open('/tmp/rag/rag_config.json','r') as f:
        rag_parameters = json.load(f)
except (Exception, KeyError) as e:
    print(f"Info: Could not load rag_config, using default config.")
    with open('/tmp/rag/default_rag_config.json','r') as f:
        rag_parameters = json.load(f)

file_path = os.path.join(os.getcwd(), "/tmp/rag/rag_config.json")
with open(file_path, "w") as f:
    json.dump(rag_parameters, f, indent=2)

vectorstore.upload_agent_config_to_upstash(filepath="/tmp/rag/rag_config.json", key="rag_config")

k = rag_parameters.get("k")
chunk_size = rag_parameters.get("chunk_size")
memory = rag_parameters.get("memory")

# logging on frontend
retriever, loaded_files_reference = vectorstore.initialize_system(adjusted_k=k, adjusted_chunk_size=chunk_size)

loaded_files_reference.extend([
    "RAG Parameters: ",
    f"Top-k value: {k}",
    f"Chunk size: {chunk_size}",
    f"Memory: {memory}"
])

crew_instance = None

class Query(BaseModel):
    question: str
    history: list[list[str]] = []

@app.on_event("startup")
def startup_event():
    global crew_instance
    crew_instance = initialize_agent()

def initialize_agent():
    load_default_agent.ConfigLoader()
    llm_setup = load_default_agent.LLMSetup()
    agent_factory = load_default_agent.DataAnalysisAgentFactory(llm_setup.llm)
    data_analysis_agent = agent_factory.create_agent()
    task_factory = load_default_agent.DataAnalysisTaskFactory(data_analysis_agent)
    data_analysis_task = task_factory.create_task()
    return Crew(
        agents=[data_analysis_agent],
        tasks=[data_analysis_task],
        verbose=True
    )

class Query(BaseModel):
    question: str
    history: list  # Expects a list of tuples like [(question, answer), ...]

@app.post("/chat")
def chat_api(query: Query):
    global disable_agent, history_mode, memory

    user_input = query.question
    conversation_history = query.history

    # Set conversation modes based on input markers
    if "/stdllm" in user_input:
        disable_agent = True
        history_mode = True
    elif "/stdllm-nh" in user_input:
        disable_agent = True
        history_mode = False
    elif "/truN" in user_input:
        disable_agent = False
        history_mode = True
    elif "/truN-nh" in user_input:
        disable_agent = False
        history_mode = False

    # Build conversation history string from the provided history (using last 'memory' turns)
    history_str = "\n".join([f"You: {q}\nAI: {a}" for q, a in conversation_history[-memory:]])
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # If the agent is enabled, use the crew_instance with context
    if not disable_agent:
        if "/truN" in user_input:
            user_input = user_input.replace("/stdllm", "")
        if "/truN-nh" in user_input:
            user_input = user_input.replace("/stdllm-nh", "")
        # Retrieve document context with error handling
        try:
            retrieved_docs = retriever.get_relevant_documents(user_input)
            context = "\n\n".join([doc.page_content for doc in retrieved_docs])
        except Exception as e:
            print("Error retrieving document context:", e)
            context = ""

        # Build the full prompt based on whether history is enabled
        if history_mode:
            full_context = f"""Context:
{context}

Conversation History:
{history_str}"""
        else:
            full_context = f"Context: {context}"

        inputs = {
            "user_question": user_input,
            "context": full_context,
            "timestamp": now_str,
        }

        try:
            result = crew_instance.kickoff(inputs=inputs)
            reply = result.tasks_output[0]
            safe_reply = str(reply) if reply is not None else "Sorry, something went wrong. Please try again."
        except Exception as e:
            safe_reply = f"Encountered an error: {e}"

    # When disable_agent is True, use the default standard llm response method
    else:
        # Remove the mode marker from the user input if present
        if "/stdllm" in user_input:
            user_input = user_input.replace("/stdllm", "")
        if "/stdllm-nh" in user_input:
            user_input = user_input.replace("/stdllm-nh", "")

        # Construct the query to include conversation history if needed
        new_query = f"I'm User. My query is: {user_input}, My Conversation History is: {history_str}"
        try:
            if history_mode:
                safe_reply = load_default_agent.StandardLLMResponse(new_query)
            else:
                safe_reply = load_default_agent.StandardLLMResponse(user_input)
        except Exception as e:
            safe_reply = f"Sorry, something went wrong. Please try again. Error details: {e}"

    return {"answer": safe_reply}

# -----------------------------
# NEW ENDPOINT: Save Agent Configuration
# -----------------------------
class AgentConfig(BaseModel):
    agent: dict
    task: dict

@app.post("/save-agent-config")
def save_agent_config(config: AgentConfig):
    try:
        # Define the file path where the configuration will be saved. Here, we save the file in the backend folder.
        file_path = os.path.join(os.getcwd(), "agents/agent_config.json")
        with open(file_path, "w") as f:
            json.dump(config.dict(), f, indent=2)
        vectorstore.upload_agent_config_to_upstash(filepath="'/tmp/agents/agent_config.json", key="agent_config")
        return {"message": "Agent configuration saved successfully.", "file_path": file_path}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/loaded-files-reference")
def get_loaded_files_reference():
    try:
        return {"loaded_files_reference": loaded_files_reference}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/initialize")
def reset_backend_state():
    global loaded_files_reference
    try:
        rag_parameters = load_default_agent.fetch_config_from_upstash("rag_config")
        file_path = os.path.join(os.getcwd(), "/tmp/rag/rag_config.json")
        with open(file_path, "w") as f:
            json.dump(rag_parameters, f, indent=2)

        k = rag_parameters.get("k")
        chunk_size = rag_parameters.get("chunk_size")
        memory = rag_parameters.get("memory")

        # logging on frontend
        retriever, loaded_files_reference = vectorstore.initialize_system(adjusted_k=k, adjusted_chunk_size=chunk_size)

        loaded_files_reference.extend([
            "RAG Parameters: ",
            f"Top-k value: {k}",
            f"Chunk size: {chunk_size}",
            f"Memory: {memory}"
        ])
    
    except (Exception, KeyError) as e:
        print(f"Info: Could not load rag_config, using default config.")
        with open('/tmp/rag/default_rag_config.json','r') as f:
            rag_parameters = json.load(f)

        k = rag_parameters.get("k")
        chunk_size = rag_parameters.get("chunk_size")
        memory = rag_parameters.get("memory")

        # logging on frontend
        retriever, loaded_files_reference = vectorstore.initialize_system(adjusted_k=k, adjusted_chunk_size=chunk_size)

        loaded_files_reference.extend([
            "",
            f"Top-k value: {k}",
            f"Chunk size: {chunk_size}",
            f"Memory: {memory}"
        ])

    return {"status": "backend state reset"}
