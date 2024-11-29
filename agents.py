import datetime
from autogen import ConversableAgent, AssistantAgent  
from config import llm_config
from utilites import executor
current_time = datetime.datetime.now() 

# Time Allocation Agent
time_allocation_agent = AssistantAgent(
            name="time_allocation_agent", 
            system_message="You are a Time Allocation Agent. "
                        f"The current system time is {current_time.strftime('%Y-%m-%d %H:%M:%S')}. " 
                        "Ask the user about task start time and duration. "
                        "When details are collected, prepare to pass them to the processor." 
                            "After getting avobe information repeat it and add"
                            "Please answer with 'TERMINATE' if I have correctly your description",
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

 

# Code Executor Agent
code_executor_agent = ConversableAgent(
    name="code_executor_agent",
    llm_config=False,
    code_execution_config={"executor": executor},
    human_input_mode="NEVER",
      default_auto_reply=
    "Please continue. If everything is done, reply 'TERMINATE'.",
)
# Time Allocation Agent
time_reallocation_agent = AssistantAgent(
    name="time_reallocation_agent", 
    system_message="You are a Time Management Assistant designed to help users track and manage their tasks efficiently. "
                   f"Current system time is {current_time.strftime('%Y-%m-%d %H:%M:%S')}. "
                   """Your goal is to:
                   - Understand the status of the user's current task
                   - If the task is incomplete, gather precise start and end times 
                   - If the task is complete, confirm and proceed with removal
                   
                   Interaction Guidelines:
                   - Ask clear, concise questions about task completion
                   - Provide context for each query
                   - Confirm details before finalizing 
                   
                   Prompt Format:
                   1. Confirm task status: 'Have you completed your task?'
                   2. If no: 'Please provide the intended start and end times for your task.'
                   3. Verify details: 'Let me confirm the task details with you.'
                   4. Seek final confirmation: 'Are these details correct? Reply with TERMINATE to confirm.'""",
    llm_config=llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "terminate" in msg.get("content").lower(),
    default_auto_reply="Please continue. If everything is complete, reply 'TERMINATE'."
)
 
# Code Processor Agent
code_processor_agent = ConversableAgent(
    name="code_processor_agent",
    system_message="Call user defined functions in a single python block without any comments."+executor.format_functions_for_prompt(),
    llm_config=llm_config, 
    human_input_mode="NEVER" ,
    default_auto_reply=  "Please continue. If everything is done, reply 'TERMINATE'.",
)

 