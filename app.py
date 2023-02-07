# flask import
from flask import Flask, request, jsonify

app = Flask(__name__)

# E:1     , I:2
# S:10    , N:20
# T:100   , F:200
# J:1000  , P:2000

mbti_point = 0

@app.route('/answer1',methods=['POST'])
def answer1():
    
    req = request.get_json()
    content = req['userRequest']['utterance']
    
    if content == u"친구들과 수다 떨며 스트레스 푸는 시간":
        mbti_point += 1
        datasend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {	
                        "simpleText": {
                            "text": "수다"
                        }
                    }
                ]
            }
        }
    else:
        mbti_point += 2
        datasend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {	
                        "simpleText": {
                            "text": "혼자"
                        }
                    }
                ]
            }
        }
    
    return jsonify(datasend)



# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
