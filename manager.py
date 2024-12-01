from autogen import  initiate_chats 
from task_scheduler import schedule_task
from task_reschedule import re_schedule_or_remove_task
 
if __name__=="__main__":
    print("Choose your workflow.")
    print("1. Schedule a task")
    print("2. Reschedule or complete a task") 

    choise = input("Enter your choise: ")
    if(choise=="1"):
        initiate_chats(schedule_task())
    if(choise=="2"):
        initiate_chats(re_schedule_or_remove_task())