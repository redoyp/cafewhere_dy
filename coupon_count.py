count = [10, 200, 300] # 0 : 스타벅스, 1 : 투썸플레이스, 2: 이디야
                        # -> 각 카페의 쿠폰 개수 세기
                        # 한정된 개수를 넘길시 쿠폰 소진 알리기 위함

def ccount(cafe_name) :
    if cafe_name == '스타벅스' :
        count[0] -= 1
        if count[0] == -1 :
            return -2
        return count[0]
    elif cafe_name == '투썸플레이스' :
        count[1] -= 1
        if count[1] == -1 :
            return -2
        return count[1]
    elif cafe_name == '이디야' :
        count[2] -= 1
        if count[2] == -1 :
            return -2
        return count[2]
      
def count_show() :
  return count
  
if __name__ == '__main__' : ## mysql test
    print(count_show())
