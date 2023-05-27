import os
import openai

def gpt(question) :
  openai.api_key =""
  limit = "50자 이내로 말해줘."
  quest = limit + question

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": quest}
    ],
    max_tokens = 50
  )

  answer = completion.choices[0].message.content
  return answer
