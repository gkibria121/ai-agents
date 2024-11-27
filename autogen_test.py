from autogen import ConversableAgent


llm_config ={
    "model" : "llama3:latest",
    "api_key" : "llama",
    "base_url" : "http://localhost:11434/v1"
}

agent = ConversableAgent(
    llm_config=llm_config,
    name="chatbot",
    human_input_mode="NEVER"
)

reply = agent.generate_reply(
    messages=[{"content" : "Tell me a fun fact about money.", "role" : "user"}]
)


print(reply)
