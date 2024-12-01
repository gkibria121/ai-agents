import datetime
from  agents import time_allocation_agent,user_proxy_agent,code_executor_agent,code_processor_agent
from autogen.coding import LocalCommandLineCodeExecutor
from pprint import pprint

# LLM Configuration
llm_config = {
    "api_type": "groq", 
    "model": "llama-3.1-70b-versatile", 
    "api_key": "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", 
    "cache_seed": None
}

 



# Chat Configuration
chats = [
    {
        "sender": time_allocation_agent,
        "recipient": user_proxy_agent,
        "message": "When can you start the task and how long will it take?",
        "summary_method": "reflection_with_llm",
        "summary_args": {
            "summary_prompt": "Extract task timing in JSON: "
                              "{'start': 'YYYY-MM-DD HH:mm', 'end' : 'YYYY-MM-DD HH:mm'   }"
        }
    },
    {
        "sender": time_allocation_agent,
        "recipient": code_processor_agent, 
        "message": "Import the add_task_reminder_function from functions, call the function with parameter start and end time",
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


def schedule_task():
   return chats

