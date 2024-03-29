# flask import
from flask import Flask, request, jsonify, Blueprint

from mbti_model import result

mbti_server = Blueprint('mbti_server', __name__)

answerlist = {}

user_mbti = {}


@mbti_server.route('/mbti_home',methods=['POST'])
def mbti_home():
    
    req = request.get_json()
    content = req['userRequest']['utterance']
    
    datasend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": "당신의 커피 취향을 알려드리는 커피TI 입니다!\n아래의 질문에 따라 답변을 입력하거나 버튼을 눌러주세요"
                    }
                },
                {	
                    "simpleText": {
                        "text": "Q1) 나에게 있어 커피 브레이크는 \n\n(1) 친구들과 수다 떨며 스트레스 푸는 시간\n(2) 조용히 혼자만의 시간을 가지며 생각을 정리하는 시간"
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "친구들과 수다 떨며 스트레스 푸는 시간",
                    "action": "message",
                    "label": "1"
                },
                {
                    "messageText": "조용히 혼자만의 시간을 가지며 생각을 정리하는 시간",
                    "action": "message",
                    "label": "2"
                },
            ]
        }
    }
    
    return jsonify(datasend)



@mbti_server.route('/answer1',methods=['POST'])
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
                        "text": "Q2) 나는 달고나 커피를 \n\n(1) 누구보다 열심히 휘저어 성공적으로 완성!!\n(2) 시도조차 하지 않는다"
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "누구보다 열심히 휘저어 성공적으로 완성!!",
                    "action": "message",
                    "label": "1"
                },
                {
                    "messageText": "시도조차 하지 않는다",
                    "action": "message",
                    "label": "2"
                },
            ]
        }
    }
    
    return jsonify(datasend)



@mbti_server.route('/answer2',methods=['POST'])
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
                        "text": "Q3) 단골 카페 나의 최애 자리는 \n\n(1) 중앙의 푹신한 소파석\n(2) 조용한 창가의 바 테이블"
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "중앙의 푹신한 소파석",
                    "action": "message",
                    "label": "1"
                },
                {
                    "messageText": "조용한 창가의 바 테이블",
                    "action": "message",
                    "label": "2"
                },
            ]
        }
    }
    
    return jsonify(datasend)



@mbti_server.route('/answer3',methods=['POST'])
def answer3():
    
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
                        "text": "Q4) 커피를 주문할 때 나는 \n\n(1) 묻고 따지지말고 당연히 아이스 아메리카노\n(2) 시그니쳐 메뉴가 무엇인지 우선 살핀다"
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "묻고 따지지말고 당연히 아이스 아메리카노",
                    "action": "message",
                    "label": "1"
                },
                {
                    "messageText": "시그니쳐 메뉴가 무엇인지 우선 살핀다",
                    "action": "message",
                    "label": "2"
                },
            ]
        }
    }
    
    return jsonify(datasend)



@mbti_server.route('/answer4',methods=['POST'])
def answer4():
    
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
                        "text": "Q5) 친구에게 선물을 준다면 나는 \n\n(1) 친구의 성향보다는 요즘 잘나가는게 최고\n(2) 평소 친구의 취향을 기억했다가 선물한다"
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "친구의 성향보다는 요즘 잘나가는게 최고",
                    "action": "message",
                    "label": "1"
                },
                {
                    "messageText": "평소 친구의 취향을 기억했다가 선물한다",
                    "action": "message",
                    "label": "2"
                },
            ]
        }
    }
    
    return jsonify(datasend)



@mbti_server.route('/answer5',methods=['POST'])
def answer5():
    
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
                        "text": "Q6) 속상한 일이 있어 친구에게 털어놓을 때 나는 \n\n(1) 아이스 커피의 얼음까지 아작아작 씹으면서 시원하게 속마음을 쏟아낸다\n(2) 따뜻한 커피 한잔과 함께 그 날 있었던 일들을 조목조목 이야기한다"
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "아이스 커피의 얼음까지 아작아작 씹으면서 시원하게 속마음을 쏟아낸다",
                    "action": "message",
                    "label": "1"
                },
                {
                    "messageText": "따뜻한 커피 한잔과 함께 그 날 있었던 일들을 조목조목 이야기한다",
                    "action": "message",
                    "label": "2"
                },
            ]
        }
    }
    
    return jsonify(datasend)



@mbti_server.route('/answer6',methods=['POST'])
def answer6():
    
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
                        "text": "Q7) 부장님이 커피를 쏜다며 커피 주문을 받을 때 나는 \n\n(1) 수고한 나를 위해 고급 스페셜티 커피를 주문한다\n(2) 부장님 따라 아메리카노를 주문한다"
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "수고한 나를 위해 고급 스페셜티 커피를 주문한다",
                    "action": "message",
                    "label": "1"
                },
                {
                    "messageText": "부장님 따라 아메리카노를 주문한다",
                    "action": "message",
                    "label": "2"
                },
            ]
        }
    }
    
    return jsonify(datasend)



@mbti_server.route('/answer7',methods=['POST'])
def answer7():
    
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
                        "text": "Q8) 친구가 우울한 목소리로 만나자고 연락이 올 때 나는 \n\n(1) 전화로 무슨 일인지 차근차근 물어본다 \n(2) 커피 한 잔 하자며 친구를 불러 이야기를 들어준다"
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "전화로 무슨 일인지 차근차근 물어본다",
                    "action": "message",
                    "label": "1"
                },
                {
                    "messageText": "커피 한 잔 하자며 친구를 불러 이야기를 들어준다",
                    "action": "message",
                    "label": "2"
                },
            ]
        }
    }
    
    return jsonify(datasend)



@mbti_server.route('/answer8',methods=['POST'])
def answer8():
    
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
                        "text": "Q9) 점심시간에 업무에 차질이 생겼다는 연락을 받았을 때 나는 \n\n(1) 차가운 커피 한잔과 함께 어떻게 해결해야 할지 차분히 생각 정리부터 한다 \n(2) 으아아아아아악! 커피 마실 새도 없이 뛰어간다"
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "차가운 커피 한잔과 함께 어떻게 해결해야 할지 차분히 생각 정리부터 한다",
                    "action": "message",
                    "label": "1"
                },
                {
                    "messageText": "으아아아아아악! 커피 마실 새도 없이 뛰어간다",
                    "action": "message",
                    "label": "2"
                },
            ]
        }
    }
    
    return jsonify(datasend)



@mbti_server.route('/answer9',methods=['POST'])
def answer9():
    
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
                        "text": "Q10) 가족과 찾은 여행지 유명 맛집에 웨이팅이 매우 긴 걸 알았을 때 나는 \n\n(1) 이곳은 맛집이니 몇 시간도 기다릴 수 있다 \n(2) 사람이 너무 많으니 근처 다른 곳으로 이동한다"
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "이곳은 맛집이니 몇 시간도 기다릴 수 있다",
                    "action": "message",
                    "label": "1"
                },
                {
                    "messageText": "사람이 너무 많으니 근처 다른 곳으로 이동한다",
                    "action": "message",
                    "label": "2"
                },
            ]
        }
    }
    
    return jsonify(datasend)



@mbti_server.route('/answer10',methods=['POST'])
def answer10():
    
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
                        "text": "Q11) 매일 아침 모닝 커피로 시작하는 내가 늦잠을 잤다면 \n\n(1) 늦더라도 커피는 못 잃어(지각...ㅜㅜ) \n(2) 사무실에 있는 믹스 커피로 대체한다"
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "늦더라도 커피는 못 잃어(지각...ㅜㅜ)",
                    "action": "message",
                    "label": "1"
                },
                {
                    "messageText": "사무실에 있는 믹스 커피로 대체한다",
                    "action": "message",
                    "label": "2"
                },
            ]
        }
    }
    
    return jsonify(datasend)



@mbti_server.route('/answer11',methods=['POST'])
def answer11():
    
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
                        "text": "Q12) 주말 아침 나는 \n\n(1) 부지런히 평일에 계획한 일들을 처리한다 \n(2) 느긋하게 늦잠 자고 일어나 브런치부터 즐긴다"
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "부지런히 평일에 계획한 일들을 처리한다",
                    "action": "message",
                    "label": "1"
                },
                {
                    "messageText": "느긋하게 늦잠 자고 일어나 브런치부터 즐긴다",
                    "action": "message",
                    "label": "2"
                },
            ]
        }
    }
    
    return jsonify(datasend)



@mbti_server.route('/answer12',methods=['POST'])
def answer12():
    
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
                        "text": "테스트가 끝났습니다!! 결과를 열어볼까요?"
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "네!!",
                    "action": "message",
                    "label": "네!!"
                }
             ]
        }
    }
    
    return jsonify(datasend)
    
    
    
@mbti_server.route('/mbti',methods=['POST'])
def mbti():
    
    req = request.get_json()
    
    user_id = req['userRequest']['user']['id']
    
    mbti_result = result(answerlist[user_id])
    user_mbti[user_id] = mbti_result
    
    print(user_mbti)
    
    if mbti_result == 'estj':
        datasend = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleText": {
                        "text": "당신의 커피TI는 ESTJ!!\n\n뜨겁게 내린 에스프레소가 어울리는 겉은 평온 속은 불타는 휴화산 CEO"
                        }
                    }
                ]
            }
        }
    elif mbti_result == 'estp':
        datasend = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleText": {
                        "text": "당신의 커피TI는 ESTP!!\n\n차가운 콜드 브루가 가장 잘 어울리는 트렌드를 향해 직진하는 8T 트럭"
                        }
                    }
                ]
            }
        }
    elif mbti_result == 'esfj':
        datasend = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleText": {
                        "text": "당신의 커피TI는 ESFJ!!\n\n차가운 카라멜 마키아토가 가장 잘 어울리는 핵인싸"
                        }
                    }
                ]
            }
        }
    elif mbti_result == 'esfp':
        datasend = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleText": {
                        "text": "당신의 커피TI는 ESFP!!\n\n따뜻하게 내린 카라멜 마키아토가 가장 어울리는 파티피플"
                        }
                    }
                ]
            }
        }
    elif mbti_result == 'entj':
        datasend = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleText": {
                        "text": "당신의 커피TI는 ENTJ!!\n\n뜨겁지 않은 에스프레소가 가장 잘 어울리는 카리스마 넘치는 야심가"
                        }
                    }
                ]
            }
        }
    elif mbti_result == 'entp':
        datasend = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleText": {
                        "text": "당신의 커피TI는 ENTP!!\n\n뜨겁게 내린 에스프레소가 가장 어울리는 프로 직진러"
                        }
                    }
                ]
            }
        }
    elif mbti_result == 'enfj':
        datasend = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleText": {
                        "text": "당신의 커피TI는 ENFJ!!\n\n아이스아메리카노가 가장 잘 어울리는 오지라퍼"
                        }
                    }
                ]
            }
        }
    elif mbti_result == 'enfp':
        datasend = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleText": {
                        "text": "당신의 커피TI는 ENFP!!\n\n뜨겁게 내린 아메리카노가 어울리는 인싸 꿈나무"
                        }
                    }
                ]
            }
        }
        
        
    elif mbti_result == 'istj':
        datasend = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleText": {
                        "text": "당신의 커피TI는 ISTJ!!\n\n따뜻한 아메리카노가 가장 잘 어울리는 인생이 FM"
                        }
                    }
                ]
            }
        }
    elif mbti_result == 'istp':
        datasend = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleText": {
                        "text": "당신의 커피TI는 ISTP!!\n\n뜨거운 아메리카노가 가장 잘 어울리는 쿨내 폭발 마이웨이"
                        }
                    }
                ]
            }
        }
    elif mbti_result == 'isfj':
        datasend = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleText": {
                        "text": "당신의 커피TI는 ISFJ!!\n\n따뜻하게 내린 카페오레가 가장 잘 어울리는 착한 꼰대"
                        }
                    }
                ]
            }
        }
    elif mbti_result == 'isfp':
        datasend = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleText": {
                        "text": "당신의 커피TI는 ISFP!!\n\n따뜻하게 내린 부드러운 아메리카노가 가장 잘 어울리는 프로 긍정러"
                        }
                    }
                ]
            }
        }
    elif mbti_result == 'intj':
        datasend = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleText": {
                        "text": "당신의 커피TI는 INTJ!!\n\n포근한 카푸치노가 가장 잘 어울리는 인공 지능 전자 두뇌"
                        }
                    }
                ]
            }
        }
    elif mbti_result == 'intp':
        datasend = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleText": {
                        "text": "당신의 커피TI는 INTP!!\n\n뜨겁지 않은 룽고가 가장 잘 어울리는 미루기 끝판왕 게으른 천재"
                        }
                    }
                ]
            }
        }
    elif mbti_result == 'infj':
        datasend = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleText": {
                        "text": "당신의 커피TI는 INFJ!!\n\n따뜻한 카페모카가 가장 잘 어울리는 겉.차.속.따"
                        }
                    }
                ]
            }
        }
    elif mbti_result == 'infp':
        datasend = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleText": {
                        "text": "당신의 커피TI는 INFP!!\n\n적당한 온도로 내린 부드러운 라떼 마키아토가 어울리는 섬세한 예술가"
                        }
                    }
                ]
            }
        }
        
    answerlist.pop(user_id)
    user_mbti.pop(user_id)
    
    return jsonify(datasend)
