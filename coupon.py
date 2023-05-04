# flask import
from flask import Flask, request, jsonify
from coupon_code_generate import coupon_code

app = Flask(__name__)

code = coupon_code()


@app.route('/coupon' ,methods=['POST'])
def coupon():

    req = request.get_json()
    content = req['userRequest']['utterance']

    user_id = req['userRequest']['user']['id']

    print(user_id)
    print(code)

    datasend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "user_id 확인"
                    }
                }
            ]
        }
    }

    return jsonify(datasend)

# 메인 함수
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
