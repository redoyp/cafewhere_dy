# flask import
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from coupon import flask_coupon
from mbti import flask_mbti

app = Flask(__name__)
api = Api(app)

api.add_resource(flask_coupon, '/')
api.add_resource(flask_mbti, '/')

# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
