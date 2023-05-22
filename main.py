# flask import
from flask import Flask, request, jsonify
from coupon import flask_coupon
from mbti import flask_mbti

app = Flask(__name__)

def coupon_run() :
  return flask_coupon()

def mbti_run() :
  return flask_mbti()

# 메인 함수
  if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
