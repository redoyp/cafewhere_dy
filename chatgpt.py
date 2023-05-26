# flask import
from flask import Flask, request, jsonify
import os
import openai

def gpt(question) :
  openai.api_key =""

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": question}
    ]
  )

  answer = completion.choices[0].message.content
  return answer


app = Flask(__name__)

@app.route('/chatgpt',methods=['POST'])
def chatgpt():
    
    req = request.get_json()
    question = req['action']['params']['research']
    answer = gpt(question)
    print(question)
    print(answer)
    
    datasend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": "테스트"
                    }
                },
                {	
                    "simpleText": {
                        "text": question + answer
                    }
                }
            ]
        }
    }
        
    
    return jsonify(datasend)
  
# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
