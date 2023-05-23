import openai
from config import *
import time
openai.api_key = OPENAI_API_KEY

print("chatGPT를 종료하려면 'bye'를 입력하세요.\n")
content = ''

while True:

    prompt = input("명령을 내려 주세요: ")
    try:
        messages = [
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': content},
            ]
        messages.append({'role': 'assistant', 'content': msg })

        messages.append({'role': 'user', 'content': prompt })
    except:
        messages = [
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': prompt},
            ]

    if prompt == 'bye':
        print("chatGPT를 종료합니다.")
        break

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )

    print(response)
    print("--------------------------------")
    print(str(response['choices'][0]['message']['content']).strip())
    msg = str(response['choices'][0]['message']['content']).strip()
    print("--------------------------------")

    time.sleep(1)

    content = content + msg
