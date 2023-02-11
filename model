def result(answerlist) :
  
  # e : 0        i : 1
  # s : 00       n : 10
  # t : 000      f : 100
  # j : 0000     p : 1000
  
  point = 0
  
  #1
  if [s for s in str if "친구들과 수다 떨며 스트레스 푸는 시간" in s] != "" : point += 0
  if [s for s in str if "조용히 혼자만의 시간을 가지며 생각을 정리하는 시간" in s] != "" : point += 1
  
  #2
  if [s for s in str if "누구보다 열심히 휘저어 성공적으로 완성" in s] != "" : point += 0
  if [s for s in str if "시도조차 하지 않는다" in s] != "" : point += 10
  
  #3
  if [s for s in str if "중앙의 푹신한 소파석" in s] != "" : point += 0
  if [s for s in str if "조용한 창가의 바 테이블" in s] != "" : point += 1
  
  #4
  if [s for s in str if "묻고 따지지말고 당연히 아이스 아메리카노" in s] != "" : point += 0
  if [s for s in str if "시그티쳐 메뉴가 무엇인지 우선 살핀다" in s] != "" : point += 100
  
  #5
  if [s for s in str if "친구의 성향보다는 요즘 잘나가는게 최고" in s] != "" : point += 0
  if [s for s in str if "평소 친구의 취향을 기억했다가 선물한다" in s] != "" : point += 10
  
  #6
  if [s for s in str if "아이스 커피의 얼음까지 아작아작 씹으면서 시원하게 속마음을 쏟아낸다" in s] != "" : point += 0
  if [s for s in str if "따뜻한 커피 한잔과 함께 그 날 있었던 일들을 조목조목 이야기한다" in s] != "" : point += 1
  
  #7
  if [s for s in str if "수고한 나를 위해 고급 스페셜티 커피를 주문한다" in s] != "" : point += 0
  if [s for s in str if "부장님 따라 아메리카노를 주문한다" in s] != "" : point += 10
  
  #8
  if [s for s in str if "전화로 무슨 일인지 차근차근 물어본다" in s] != "" : point += 0
  if [s for s in str if "커피 한 잔 하자며 친구를 불러 이야기를 들어준다" in s] != "" : point += 100
  
  #9
  if [s for s in str if "차가운 커피 한잔과 함께 어떻게 해결해야 할지 차분히 생각 정리부터 한다" in s] != "" : point += 0
  if [s for s in str if "커피 마실 새도 없이 뛰어간다" in s] != "" : point += 1000
  
  #10
  if [s for s in str if "이곳은 맛집이니 몇시간도 기다릴 수 있다" in s] != "" : point += 0
  if [s for s in str if "사람이 너무 많으니 근처 다른 곳으로 이동한다" in s] != "" : point += 1000
  
  #11
  if [s for s in str if "늦더라도 커피는 못 잃어" in s] != "" : point += 0
  if [s for s in str if "사무실에 있는 믹스 커피로 대체한다" in s] != "" : point += 100
  
  #12
  if [s for s in str if "부지런히 평일에 계획한 일들을 처리한다" in s] != "" : point += 0
  if [s for s in str if "느긋하게 늦잠 자고 일어나 브런치부터 즐겨본다" in s] != "" : point += 1000
  
  

  ie = point // 1000
  ns = point % 1000 // 100
  ft = point % 100 // 10
  pj = point % 10
  
  
  
  if (0 <= ie and ie <= 1) and (0 <= ns and ns <= 1) and (0 <= ft and ft <= 1) and (0 <= pj and pj <= 1):
    mbti_result = 'estj'
    
  if (0 <= ie and ie <= 1) and (0 <= ns and ns <= 1) and (0 <= ft and ft <= 1) and (2 <= pj and pj <= 3):
    mbti_result = 'estp'
    
  if (0 <= ie and ie <= 1) and (0 <= ns and ns <= 1) and (2 <= ft and ft <= 3) and (0 <= pj and pj <= 1):
    mbti_result = 'esfj'
    
  if (0 <= ie and ie <= 1) and (0 <= ns and ns <= 1) and (2 <= ft and ft <= 3) and (2 <= pj and pj <= 3):
    mbti_result = 'esfp'
    
  if (0 <= ie and ie <= 1) and (2 <= ns and ns <= 3) and (0 <= ft and ft <= 1) and (0 <= pj and pj <= 1):
    mbti_result = 'entj'
    
  if (0 <= ie and ie <= 1) and (2 <= ns and ns <= 3) and (0 <= ft and ft <= 1) and (2 <= pj and pj <= 3):
    mbti_result = 'entp'
    
  if (0 <= ie and ie <= 1) and (2 <= ns and ns <= 3) and (2 <= ft and ft <= 3) and (0 <= pj and pj <= 1):
    mbti_result = 'enfj'
    
  if (0 <= ie and ie <= 1) and (2 <= ns and ns <= 3) and (2 <= ft and ft <= 3) and (2 <= pj and pj <= 3):
    mbti_result = 'enfp'
    
  if (2 <= ie and ie <= 3) and (0 <= ns and ns <= 1) and (0 <= ft and ft <= 1) and (0 <= pj and pj <= 1):
    mbti_result = 'istj'
    
  if (2 <= ie and ie <= 3) and (0 <= ns and ns <= 1) and (0 <= ft and ft <= 1) and (2 <= pj and pj <= 3):
    mbti_result = 'istp'
    
  if (2 <= ie and ie <= 3) and (0 <= ns and ns <= 1) and (2 <= ft and ft <= 3) and (0 <= pj and pj <= 1):
    mbti_result = 'isfj'
    
  if (2 <= ie and ie <= 3) and (0 <= ns and ns <= 1) and (2 <= ft and ft <= 3) and (2 <= pj and pj <= 3):
    mbti_result = 'isfp'
    
  if (2 <= ie and ie <= 3) and (2 <= ns and ns <= 3) and (0 <= ft and ft <= 1) and (0 <= pj and pj <= 1):
    mbti_result = 'intj'
    
  if (2 <= ie and ie <= 3) and (2 <= ns and ns <= 3) and (0 <= ft and ft <= 1) and (2 <= pj and pj <= 3):
    mbti_result = 'intp'
    
  if (2 <= ie and ie <= 3) and (2 <= ns and ns <= 3) and (2 <= ft and ft <= 3) and (0 <= pj and pj <= 1):
    mbti_result = 'infj'
    
  if (2 <= ie and ie <= 3) and (2 <= ns and ns <= 3) and (2 <= ft and ft <= 3) and (2 <= pj and pj <= 3):
    mbti_result = 'infp'
    
  return mbti_result
