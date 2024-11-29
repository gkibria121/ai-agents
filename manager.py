import datetime
from autogen import ConversableAgent, AssistantAgent, UserProxyAgent, initiate_chats
from autogen.coding import LocalCommandLineCodeExecutor
from pprint import pprint
from task_scheduler import schedule_task
from task_reschedule import re_schedule_or_remove_task
 
if __name__=="__main__":
    print("Choose your workflow.")
    print("1. Schedule a task")
    print("2. Reschedule a task")
    print("3. Complete a task")

    choise = input("Enter your choise: ")
    if(choise=="1"):
        initiate_chats(schedule_task())
    if(choise=="2"):
        initiate_chats(re_schedule_or_remove_task())