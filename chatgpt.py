import os
import openai
import chatgpt_response

openai.api_key =""
question = content

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": content}
  ]
)

answer = completion.choices[0].message.content
