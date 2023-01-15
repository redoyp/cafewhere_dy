# flask import
from flask import Flask, request, jsonify

app = Flask(__name__)


answer = 0


@app.route('/ans1',methods=['POST'])
def ans1():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": 'test'
                    }
                }
            ]
        }
    }





# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
