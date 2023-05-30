# flask import
from flask import Flask
from chatgpt import gpt_server
from coupon import coupon_server
from mbti import mbti_server
from recommend import recommend_server

app = Flask(__name__)

app.register_blueprint(gpt_server)
app.register_blueprint(coupon_server)
app.register_blueprint(mbti_server)
app.register_blueprint(recommend_server)

# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
