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
        
