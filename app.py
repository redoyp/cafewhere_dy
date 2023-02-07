# flask import
from flask import Flask, request, jsonify

app = Flask(__name__)

answerlist = {}

@app.route('/answer1',methods=['POST'])
def answer1():
    
    req = request.get_json()
    content = req['userRequest']['utterance']
    
    user_id = req['userRequest']['user']['id']
    answerlist[user_id] = []
    
    answerlist[user_id].append(content)
    print(answerlist)
    
    datasend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": "Q2.나는 달고나 커피를 \n\n(1) 누구보다 열심히 휘저어 성공적으로 완성!!\n(2) 시도조차 하지 않는다"
                    }
                }
            ]
        }
    }
    
    return jsonify(datasend)



@app.route('/answer2',methods=['POST'])
def answer2():
    
    req = request.get_json()
    content = req['userRequest']['utterance']
    
    user_id = req['userRequest']['user']['id']
    
    answerlist[user_id].append(content)
    
    print(answerlist)
    
    datasend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": "Q3.단골 카페 나의 최애 자리는 \n\n(1) 중앙의 푹신한 소파석\n(2) 조용한 창가의 바 테이블"
                    }
                }
            ]
        }
    }
    
    return jsonify(datasend)



@app.route('/answer3',methods=['POST'])
def answer2():
    
    req = request.get_json()
    content = req['userRequest']['utterance']
    
    user_id = req['userRequest']['user']['id']
    
    answerlist[user_id].append(content)
    
    print(answerlist)
    
    datasend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": "Q4.커피를 주문할 때 나는 \n\n(1) 묻고 따지지말고 당연히 아이스 아메리카노\n(2) 시그니쳐 메뉴가 무엇인지 우선 살핀다"
                    }
                }
            ]
        }
    }
    
    return jsonify(datasend)



@app.route('/answer4',methods=['POST'])
def answer2():
    
    req = request.get_json()
    content = req['userRequest']['utterance']
    
    user_id = req['userRequest']['user']['id']
    
    answerlist[user_id].append(content)
    
    print(answerlist)
    
    datasend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": "Q5.친구에게 선물을 준다면 나는 \n\n(1) 친구의 성향보다는 요즘 잘나가는게 최고\n(2) 평소 친구의 취향을 기억했다가 선물한다"
                    }
                }
            ]
        }
    }
    
    return jsonify(datasend)



@app.route('/answer5',methods=['POST'])
def answer2():
    
    req = request.get_json()
    content = req['userRequest']['utterance']
    
    user_id = req['userRequest']['user']['id']
    
    answerlist[user_id].append(content)
    
    print(answerlist)
    
    datasend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": "Q6.속상한 일이 있어 친구에게 털어놓을 때 나는 \n\n(1) 아이스 커피의 얼음까지 아작아작 씹으면서 시원하게 속마음을 쏟아낸다\n(2) 따뜻한 커피 한잔과 함께 그 날 있었던 일등을 조목조목 이야기한다"
                    }
                }
            ]
        }
    }
    
    return jsonify(datasend)



@app.route('/answer6',methods=['POST'])
def answer2():
    
    req = request.get_json()
    content = req['userRequest']['utterance']
    
    user_id = req['userRequest']['user']['id']
    
    answerlist[user_id].append(content)
    
    print(answerlist)
    
    datasend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": "Q7.부장님이 커피를 쏜다며 커피 주문을 받을 때 나는 \n\n(1) 수고한 나를 위해 고급 스페셜티 커피를 주문한다.\n(2) 부장님 따라 아메리카노를 주문한다."
                    }
                }
            ]
        }
    }
    
    return jsonify(datasend)


# 메인 함수
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
