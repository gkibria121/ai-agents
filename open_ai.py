from openai import OpenAI

client = OpenAI(
  base_url="http://localhost:11434/v1",
  api_key="ollama" 
)

completion = client.chat.completions.create(
  model="llama3",
  messages=[{"role": "user", "content": "Hello"}]
)

print(completion.choices[0].message.content)