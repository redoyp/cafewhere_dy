# flask import
from flask import Flask, request, jsonify

app = Flask(__name__)

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

# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
