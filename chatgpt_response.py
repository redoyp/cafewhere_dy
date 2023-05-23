# flask import
from flask import Flask, request, jsonify
import chatgpt

app = Flask(__name__)

@app.route('/chatgpt_response',methods=['POST'])
def mbti_home():
    
    req = request.get_json()
    content = req['userRequest']['utterance']
    
    datasend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": answer
                    }
                }
            ]
        }
    }
    
    return jsonify(datasend)
  
# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
