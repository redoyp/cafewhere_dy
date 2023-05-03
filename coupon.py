# flask import
from flask import Flask, request, jsonify

from mbti_model import result

app = Flask(__name__)

user_coupon = {}


@app.route('/coupon',methods=['POST'])
def coupon():
    
    req = request.get_json()
    content = req['userRequest']['utterance']
    
    user_id = req['userRequest']['user']['id']
    user_coupon[user_id] = []
    
    user_coupon[user_id].append(content)
    print(user_id)
    
    datasend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": "user_id 확인"
                    }
                }
            ]
        }
    }
    
    return jsonify(datasend)

# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
