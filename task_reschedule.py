
from agents import time_reallocation_agent,user_proxy_agent,code_executor_agent,code_processor_agent


# Chat Configuration
chats = [
    {
        "sender": time_reallocation_agent,
        "recipient": user_proxy_agent,
        "message": "Let's review your task status. Have you completed the task you were working on?",
        "summary_method": "reflection_with_llm",
        "summary_args": {
            "summary_prompt": "Analyze the user's response and generate a JSON representing task status:\n"
                              "- If task is completed: {'status': 'completed'}\n"
                              "- If task is incomplete: {\n"
                              "    'status': 'incomplete',\n"
                              "    'start': 'YYYY-MM-DD HH:mm',\n"
                              "    'end': 'YYYY-MM-DD HH:mm'\n"
                              "  }"
        }
    },
        {
        "sender": time_reallocation_agent,
        "recipient": code_processor_agent, 
        "message": "Based on the task status JSON, call the appropriate task management function.",
        "summary_method": "reflection_with_llm", 
        "summary_args": {
            "summary_prompt": "If status is 'incomplete', generate Python block importing update_task_reminder from functions and call it. "
                            "If status is 'completed', generate Python block importing remove_task_reminder from functions and call it. "
                            "Provide only the Python code block without comments."
        },
        "max_turns": 1
    },
    {
        "sender": code_processor_agent,
        "recipient": code_executor_agent,
        "message": "Execute task reminder function",
        "summary_method": "reflection_with_llm",  
        "max_turns" : 1
    }
]


 
def re_schedule_or_remove_task():
   return chats