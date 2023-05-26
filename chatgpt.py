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
    
    if question == '끝' :
      datasend = {
          "version": "2.0",
          "template": {
              "outputs": [
                  {	
                      "simpleText": {
                          "text": '만나서 반가웠어요~'
                      }
                  }
              ]
          }
      }
    else :
      datasend = {
          "version": "2.0",
          "template": {
              "outputs": [
                  {	
                      "simpleText": {
                          "text": answer
                      }
                  },
                  {	
                      "simpleText": {
                          "text": "궁금한 점이 더 있으신가요??"
                      }
                  }
              ],
              "quickReplies": [
                  {
                      "label": "네",
                      "action": "block",
                      "blockId": "646d0039261683267f04dd38"
                  },
                  {
                      "label": "아니요",
                      "action": "block",
                      "blockId": "63be8e5413b6a940ee25dfa0"
                  },
              ]
          }
      }
        
    
    return jsonify(datasend)
  
# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
