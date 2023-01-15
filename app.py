# flask import
from flask import Flask, request, jsonify

app = Flask(__name__)


answer = 0


@app.route('/answer1',methods=['POST'])
def ans1():
  prob1_buttons : ['친구들과 수다 떨며 스트레스 푸는 시간', '조용히 혼자만의 시간을 가지며 생각을 정리하는 시간']
  response = {
    "message" : {
      "text" : '나에게 있어 커피 브레이크는?'
    },
    "keyboard" : {
      "type" : "buttons",
      "buttons" : prob1_buttons
    }
  }
    
  return response





# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
