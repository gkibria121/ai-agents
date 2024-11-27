llm_config =  {"api_type": "groq", "model": "llama-3.1-70b-versatile", "api_key": "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", "cache_seed": None}

# Command Line Executor
from autogen.code_utils import create_virtual_env
from autogen.coding import CodeBlock, LocalCommandLineCodeExecutor
from autogen import ConversableAgent

venv_dir = ".env_llm"
venv_context = create_virtual_env(venv_dir)
def add(a,b):
    """
    This function adds two numbers and returns a number.

    Parameters :
    a (int) : This is a number
    b (int) : This is a number

    Returns:
    (int) sub of a and b
    """
    return a+b
executor = LocalCommandLineCodeExecutor(
    virtual_env_context=venv_context,
    timeout=200,
    work_dir="coding",
    functions=[add]
)
 



# ---

# Agent 1: Code Writer agent
from autogen import AssistantAgent

# Agent that writes code
code_writer_agent = AssistantAgent(
    name="code_writer_agent",
    llm_config=llm_config,
    code_execution_config=False,
    human_input_mode="NEVER",
)
 
code_writer_system_message = code_writer_agent.system_message+executor.format_functions_for_prompt()

 
code_writer_agent = ConversableAgent(
    name="code_writer_agent",
    llm_config=llm_config,
    code_execution_config=False,
    human_input_mode="NEVER",
    system_message=code_writer_system_message,
)

# Agent that executes code
code_executor_agent = ConversableAgent(
    name="code_executor_agent",
    llm_config=False,
    code_execution_config={"executor": executor},
    human_input_mode="ALWAYS",
   
    default_auto_reply=
    "Please continue. If everything is done, reply 'TERMINATE'.",
)

# ---

# Coding Task
import datetime

today = datetime.datetime.now().date()

message = f"Talk to me with interesting topics, If i say I am seek, give me user defined funciton in python block."

# Let's define the chat and initiate it !
chat_result = code_executor_agent.initiate_chat(
    code_writer_agent,
    message=message
)