# flask import
from flask import Flask, request, jsonify

app = Flask(__name__)
answerlist = {}




# 서버가 정상적으로 작동하는지 확인
# gttps : //url.com
@app.route("/")
def hello():
  return "Hello, Flask!"




# https://url.com/coffee
@app.route('/coffe', methods=['POST'])
def coffe(): # 함수 선언
  req = request.get_json()
  
  coffe_menu = req["action"]["detailParams"]["coffe_menu"]["value"] # json파일 읽기
  
  answer = coffe_menu
  # answer = "아메리카노"
  
      # 답변 설정
  res = {
    "version" : "2.0",
    "template": {
      "outputs": [
        {
          "simpleText": {
            "text" : answer
          }
        }
      ]
    }
  }
  
  # 답변
  return jsonify(res)
# 이 라인을 기준으로 위에는 제가 따로 연습할려고 사용한 부분입니다...





@app.route('/answer1',methods=['POST'])
def coffeeTI_message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    
    if content == "MBTI"|"mbti"|"테스트"|"커피 테스트"|"커피테스트"|"커피 mbti"|"커피mbti"|"커피 MBTI"|"커피MBTI"|"커피 TI"|"커피TI" {
      dataSend = {
        "message" : {
         "text" : "당신의 커피 취향을 알려드리는 커피TI 입니다!! 다음의 질문에 따라 답변해주세요!!"
         "text" : "Q1. 나에게 있어 커피 브레이크는?"
          "text" : "(1) 친구들과 수다 떨며 스트레스 푸는 시간"
          "text" : "(2) 조용히 혼자만의 시간을 가지며 생각을 정리하는 시간"
       }
     }
    }
    
    return jsonify(datasend)


def ans1():
  
    req = request.get_json()
    content = req['userRequest']
    content = content['utterance']
    param= req['action']['detailParams']
    answer1 = param['answer1']['value'] 
    answer2 = param['answer2']['value']
    
    user_id = req['userRequest']['user']['id']
    answerlist[user_id] = []
    
    answerlist[user_id].append(answer1)
    answerlist[user_id].append(answer2)
    
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
