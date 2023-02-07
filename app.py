# flask import
from flask import Flask, request, jsonify

app = Flask(__name__)

answerlist = {}

@app.route('/answer1',methods=['POST'])
def answer1():
    
    req = request.get_json()
    content = req['userRequest']['utterance']
    
    if content == u"시작하기":
        dataSend ={
            "message" : {
                "text" : "시작하기 테스트입니다."
            }
        }

    elif content == u"안녕하세요":
        dataSend ={
            "message" : {
                "text" : "반갑습니다 어서오세요."
            }
        }
    
    return jsonify(dataSend)



# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
