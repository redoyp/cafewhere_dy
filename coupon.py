# flask import
from flask import Flask, request, jsonify
from coupon_db import *
from coupon_code_generate import *

app = Flask(__name__)

user_code = coupon_dup()

@app.route('/coupon' ,methods=['POST'])
def coupon():

    req = request.get_json()
    cafe_name = req['userRequest']['utterance']

    user_id = req['userRequest']['user']['id']

    print(user_id)
    print(user_code)
    print(cafe_name)

    dup = getCouponCode(user_id, cafe_name)

    if user_code == dup :
        datasend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "이미 해당 카페의 쿠폰을 받았어요ㅜㅜ"
                        }
                    }
                ]
            }
        }
    else :
        insCoupon(user_id, user_code, cafe_name)
        datasend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": cafe_name + "카페의 쿠폰 코드에요!!\n\n" + user_code
                        }
                    }
                ]
            }
        }

    return jsonify(datasend)


# 메인 함수
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)