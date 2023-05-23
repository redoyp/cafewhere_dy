# flask import
from flask import Flask, request, jsonify
from coupon_db import *
from coupon_code_generate import *

app = Flask(__name__)

user_code = coupon_dup()

count = [0, 200, 300]  # 스타벅스, 투썸플레이스, 이디야 순서로 쿠폰 개수 제한

@app.route('/coupon' ,methods=['POST'])
def coupon():

    req = request.get_json()
    cafe_name = req['userRequest']['utterance']

    user_id = req['userRequest']['user']['id']

    print(user_id, user_code, cafe_name)
    print(getCouponIDCafe(user_id, cafe_name))
    
    if cafe_name == '스타벅스' :
        limit = count[0]
    elif cafe_name == '투썸플레이스' :
        limit = count[1]
    elif cafe_name == '이디야' :
        limit = count[2]
    

    if getCouponIDCafe(user_id, cafe_name) == 1 :
        datasend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "이미 해당 카페의 쿠폰을 받았어요ㅜㅜ\n받으신 " + cafe_name + "의 쿠폰 코드는\n\n" + getCouponCode(user_id, cafe_name) + "\n\n이에요"
                        }
                    }
                ]
            }
        }
    else :
        if getCouponCount(cafe_name) >= limit :
            print(getCouponCount(cafe_name), limit)
            datasend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": cafe_name + " 카페의 쿠폰이 모두 소진됐어요ㅜㅜ"
                            }
                        }
                    ]
                }
            }
        else :
            insCoupon(user_id, user_code, cafe_name)
            print(getCouponCount(cafe_name), limit)
            datasend = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": cafe_name + " 카페의 쿠폰 코드에요!!\n\n" + user_code
                            }
                        }
                    ]
                }
            }

    return jsonify(datasend)


# 메인 함수
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
