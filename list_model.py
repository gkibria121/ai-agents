from autogen import Client

# Initialize the AutoGen client
client = Client(api_key="llama")

# Fetch the list of available models
models = client.get_available_models()

# Print the models
print("Available Models:")
for model in models:
    print(model)
