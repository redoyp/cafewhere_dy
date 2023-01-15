# flask import
from flask import Flask, request, jsonify

app = Flask(__name__)


answer = 0


@app.route('/answer1',methods=['POST'])
def ans1():
  body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "당신의 커피 취향을 알려드리는 커피TI입니다."
                    }
                }
            ]
        }
    }

    return responseBody



# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
