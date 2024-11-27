from autogen import ConversableAgent
from pprint import pprint
import os

llm_config =  {"api_type": "groq", "model": "llama3-8b-8192", "api_key": "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", "cache_seed": None}
# llm_config ={
#     "model" : "llama2:13b",
#     "api_key" : "llama",
#     "base_url" : "http://localhost:11434/v1"
# }
bret = ConversableAgent(
    llm_config=llm_config,
    name="bret",  
    system_message="Your name is Bret and you are a stand-up comedian in a two-person comedy show. when you're ready to end the conversation, say 'I gotta go'.",
    is_termination_msg=lambda msg: "I gotta go" in msg
    ["content"]  )

jemaine = ConversableAgent(
    llm_config=llm_config,
    name="jemaine", 
    system_message="Your name is Jemaine and you are a stand-up comedian in a two-person comedy show. when you're ready to end the conversation, say 'I gotta go'.",
     is_termination_msg=lambda msg: "I gotta go" in msg["content"] 
    )
 

chat = bret.initiate_chat(
recipient = jemaine,
message="Jemaine, let's keep the jokes rolling, Let's start with jokes about cats.",
max_turns = 2 
)

reply = jemaine.send(message="What was the last joke we talked about?", recipient=bret)


print(reply)