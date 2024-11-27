import json
import os
from typing import Literal

from typing_extensions import Annotated

import autogen

config_list = [
    {"api_type": "groq", "model": "llama3-8b-8192", "api_key": "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", "cache_seed": None}
]

# Create the agent for tool calling
chatbot = autogen.AssistantAgent(
    name="chatbot",
    system_message="""For currency exchange and weather forecasting tasks,
        only use the functions you have been provided with.
        Output 'HAVE FUN!' when an answer has been provided.""",
    llm_config={"config_list": config_list},
)

# Note that we have changed the termination string to be "HAVE FUN!"
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    is_termination_msg=lambda x: x.get("content", "") and "HAVE FUN!" in x.get("content", ""),
    human_input_mode="NEVER",
    max_consecutive_auto_reply=1,
)