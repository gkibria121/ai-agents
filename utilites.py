# Local code executor

from autogen.coding import LocalCommandLineCodeExecutor
from functions import update_task_reminder,remove_task_reminder, add_task_reminder
executor = LocalCommandLineCodeExecutor(
    timeout=200,
    work_dir="coding",
    functions=[update_task_reminder,remove_task_reminder,add_task_reminder]
)
