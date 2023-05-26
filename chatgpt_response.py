# flask import
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chatgpt_response',methods=['POST'])
def chatgpt_response():
    
    req = request.get_json()
    content = req['userRequest']['utterance']
    question = req['action']['params']
    print(question, content)
    
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
                        "text": content
                    }
                }
            ]
        }
    }
        
    
    return jsonify(datasend)
  
# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
