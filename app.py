# flask import
from flask import Flask, request, jsonify

app = Flask(__name__)

answerlist = {}

@app.route('/answer1',methods=['POST'])
def answer1():
    
    req = request.get_json()
    content = req['userRequest']['utterance']
    
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
    
    return jsonify(dataSend)



# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
