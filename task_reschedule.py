import datetime
from autogen import ConversableAgent, AssistantAgent, UserProxyAgent, initiate_chats
from autogen.coding import LocalCommandLineCodeExecutor
from pprint import pprint
# Utility function to be called
def update_task_reminder(start, end):
    """
    Print task details.

    Parameters:
    start (str): Task start date and time in string format.
    end (str): Task end date and time in string format. 

    Returns:
    None
    """
    print(f"Task Start: {start}")
    print(f"Task End: {end}") 

def remove_task_reminder():
    """
    Print task details.

    Parameters:
        no parameters
    Returns:
    None
    """ 
    print("task is completed")

# LLM Configuration
llm_config = {
    "api_type": "groq", 
    "model": "llama-3.1-70b-versatile", 
    "api_key": "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", 
    "cache_seed": None
}

# Local code executor
executor = LocalCommandLineCodeExecutor(
    timeout=200,
    work_dir="coding",
    functions=[update_task_reminder,remove_task_reminder]
)


current_time = datetime.datetime.now()

# Time Allocation Agent
time_allocation_agent = AssistantAgent(
            name="time_allocation_agent", 
            system_message="You are a Time Re-Allocation Agent. "
                        f"The current system time is {current_time.strftime('%Y-%m-%d %H:%M:%S')}. " 
                        "Ask the user whether  task is done or not. "
                        "If he has done the task , do not ask him when he can start and duration"
                        "If he did not done the task "
                         "Ask the user when can  start task  and duration. "
                        "After getting avobe information repeat it and add"
                        "Please answer with 'TERMINATE' if I have correctly your description" 
                        ,
                        
            llm_config=llm_config,
            human_input_mode="NEVER",
            is_termination_msg=lambda msg: "terminate" in msg.get("content").lower(),
            default_auto_reply=  "Please continue. If everything is done, reply 'TERMINATE'.",
        )      


# User Proxy Agent
user_proxy_agent = ConversableAgent(
    name="user_proxy_agent",
    human_input_mode="ALWAYS", 
    llm_config=False
)

# Code Processor Agent
code_processor_agent = ConversableAgent(
    name="code_processor_agent",
    system_message="Call user defined functions in a single python block without any comments."+executor.format_functions_for_prompt(),
    llm_config=llm_config, 
    human_input_mode="NEVER" ,
    default_auto_reply=  "Please continue. If everything is done, reply 'TERMINATE'.",
)

# Code Executor Agent
code_executor_agent = ConversableAgent(
    name="code_executor_agent",
    llm_config=False,
    code_execution_config={"executor": executor},
    human_input_mode="NEVER",
      default_auto_reply=
    "Please continue. If everything is done, reply 'TERMINATE'.",
)

# Chat Configuration
chats = [
    {
        "sender": time_allocation_agent,
        "recipient": user_proxy_agent,
        "message": "Have you finished your task?",
        "summary_method": "reflection_with_llm",
        "summary_args": {
            "summary_prompt": "If user did complete his task"
            "Give me the JSON"
            "{  status : 'completed'  }"
            "If user did not complete the task"
            "Extract task timing in JSON: "
                              "{'start': 'YYYY-MM-DD HH:mm', 'end' : 'YYYY-MM-DD HH:mm' , status : 'incomplete'  }"
        }
    },
    {
        "sender": time_allocation_agent,
        "recipient": code_processor_agent, 
        "message": """ 
        If the status of JSON object is incomplete , you will write a python block importing update_task_reminder from functions and call it with start and end time
        If the status of JSON object is completed , you will write a python block importing remove_task 

        """,
        "summary_method": "reflection_with_llm", 
        "summary_args": {
            "summary_prompt": "Only python block  , without any comment or explain "
                               
        }   ,
        "max_turns" : 1
    },
    {
        "sender": code_processor_agent,
        "recipient": code_executor_agent,
        "message": "Execute task reminder function",
        "summary_method": "reflection_with_llm",  
        "max_turns" : 1
    }
]


 

initiate_chats(chats)