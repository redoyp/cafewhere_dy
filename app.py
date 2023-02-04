# flask import
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/answer1',methods=['POST'])
def answer1():
    
    content = request.get_json()                       # 사용자가 입력한 정보를 json형태로 가져옴
    content = content['userRequest']['utterance']      # 입력한 발화를 가져옴
    
    if content == u"친구들과 수다 떨며 스트레스 푸는 시간":
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {	
                        "simpleText": {
                            "text": "test"
                        }
                    }
                ]
            }
        }

    return response



# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
