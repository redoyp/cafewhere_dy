# flask import
from flask import Flask, request, jsonify

app = Flask(__name__)

answerlist = {}

@app.route('/answer1',methods=['POST'])
def answer1():
    
    req = request.get_json()
    content = req['userRequest']['utterance']
    
    user_id = req['userRequest']['user']['id']
    answerlist[user_id] = []
    
    answerlist[user_id].append(content)
    
    print(answerlist)
    
    if content == u"친구들과 수다 떨며 스트레스 푸는 시간":
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
