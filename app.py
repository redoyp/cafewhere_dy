# flask import
from flask import Flask, request, jsonify

app = Flask(__name__)


answerlist = {}


@app.route('/prob1',methods=['POST'])
def ans1():
    req = request.get_json()
    content = req['userRequest']
    content = content['utterance']
    param= req['action']['detailParams']
    answer1-1 = param['ans1-1']['value'] 
    answer1-2 = param['ans1-2']['value']
    
    user_id = req['userRequest']['user']['id']
    answerlist[user_id] = []
    
    answerlist[user_id].append(answer1-1)
    answerlist[user_id].append(answer1-2)
    
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": '{}'.format(answerlist[user_id]) 
                    }
                }
            ]
        }
    }

    return response



# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
