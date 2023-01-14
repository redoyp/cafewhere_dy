# flask import
from flask import Flask, request, jsonify

app = Flask(__name__)
answerlist = {}




# 서버가 정상적으로 작동하는지 확인
# gttps : //url.com
@app.route("/")
def hello_prac():
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


answer = 0


@app.route('/answer1',methods=['POST'])
def ans1():
  prob1_buttons : ['친구들과 수다 떨며 스트레스 푸는 시간', '조용히 혼자만의 시간을 가지며 생각을 정리하는 시간']
  
    dataReceive = request.get_json()
    user_input = dataReceive["content"]
    response = {
      "message" : {
        "text" : '나에게 있어 커피 브레이크는?'
      },
      "keyboard" : {
        "type" : "buttons",
        "buttons" : prob1_buttons
      }
    }
    if user_input == prob1_buttons[0]: answer += 1
      elif user_input == prob1_buttons[1]: answer += 2
    

    return response, answer





# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
