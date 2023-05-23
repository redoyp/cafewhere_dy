import os
import openai

openai.api_key = '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'

question = input("무엇을 물어볼까요?: ")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": question}
  ]
)

print(completion.choices[0].message.content)
