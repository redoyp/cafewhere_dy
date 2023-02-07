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
    
    datasend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": "Q2.나는 달고나 커피를 \n\n(1) 누구보다 열심히 휘저어 성공적으로 완성\n(2) 시도조차 하지 않는다"
                    }
                }
            ]
        }
    }
    
    return jsonify(datasend)



@app.route('/answer2',methods=['POST'])
def answer2():
    
    req = request.get_json()
    content = req['userRequest']['utterance']
    
    user_id = req['userRequest']['user']['id']
    answerlist[user_id] = []
    
    answerlist[user_id].append(content)
    
    print(answerlist)
    
    datasend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": "ok"
                    }
                }
            ]
        }
    }
    
    return jsonify(datasend)


# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
