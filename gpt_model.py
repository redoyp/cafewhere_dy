import os
import openai

def gpt(question) :
  openai.api_key =""

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": question}
    ],
    max_tokens = 50
  )

  answer = completion.choices[0].message.content
  return answer
