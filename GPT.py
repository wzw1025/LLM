from openai import OpenAI

client = OpenAI(api_key="sk-CLSYtiq5EclonZRD6b8503E7A25b414383A0D1B5B6Bc41C4", base_url="https://api.pla.wiki/v1")

response = client.chat.completions.create(
    model="moonshot-v1-32k",
    messages=[
        {"role": "system", "content": "你是一名数学老师"},
        {"role": "user", "content": "1+1"},
    ],
    stream=False
)

print(response.choices[0].message.content)