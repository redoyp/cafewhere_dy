# flask import
from flask import Flask, request, jsonify

app = Flask(__name__)

mbti_ans = 0

@app.route('/answer1',methods=['POST'])
def answer1():
    
    content = request.get_json()
    content = content['userRequest']['utterance']
    
    if content == u"친구들과 수다 떨며 스트레스 푸는 시간":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "수다"
                        }
                    }
                ]
            }
        }
        mbti_ans += 0
    elif content == u"조용히 혼자만의 시간을 가지며 생각을 정리하는 시간":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "혼자"
                        }
                    }
                ]
            }
        }
        mbti_ans += 1
    else:
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "error"
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)



# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
