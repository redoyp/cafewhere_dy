# flask import
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/answer1',methods=['POST'])
def answer1():
    
    content = request.get_json()
    content = content['userRequest']['utterance']
    content=content.replace("\n","")
    print(content)
    
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": "test"
                    }
                }
            ]
        }
    }

    return response



# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
