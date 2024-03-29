from flask import Flask, request, jsonify
import pymysql

def __init__(self) :
    pass


def getCoupon() : # table 확인 -> 안 쓸 듯
    ret = []

    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '1223334444',
                       db = 'cafewhere_coupon_db',
                       charset = 'utf8')


    cur = conn.cursor()

    sql = "select * from coupon";
    cur.execute(sql)

    rows = cur.fetchall()
    for e in rows:
        temp = {'id': e[0], 'code': e[1], 'cafe': e[2]}
        ret.append(temp)

    conn.commit()
    conn.close()
    return ret
    
    
def delAll() : # table에서 모두 삭제
    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '1223334444',
                       db = 'cafewhere_coupon_db',
                       charset = 'utf8')


    cur = conn.cursor()

    sql = 'truncate coupon'

    cur.execute(sql)

    conn.commit()
    conn.close()


def getCode_fordup() : # coupon_code_generate 에서 같은 코드 생성 방지
    ret = []

    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '1223334444',
                       db = 'cafewhere_coupon_db',
                       charset = 'utf8')


    cur = conn.cursor()

    sql = "select code from coupon";
    cur.execute(sql)

    codes = cur.fetchall()
    for i in codes:
        ret.append(i)

    conn.commit()
    conn.close()
    return ret



def insCoupon(user_id, user_code, cafe_name) : # table에 삽입
    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '1223334444',
                       db = 'cafewhere_coupon_db',
                       charset = 'utf8')


    cur = conn.cursor()

    sql = '''insert into coupon (id, code, cafe) values (%s, %s, %s)'''

    cur.execute(sql, (user_id, user_code, cafe_name))

    conn.commit()
    conn.close()
    
    

def delCoupon(user_id, user_code, cafe_name) : # table에서 삭제
    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '1223334444',
                       db = 'cafewhere_coupon_db',
                       charset = 'utf8')


    cur = conn.cursor()

    sql = 'delete from coupon where id = %s AND code = %s AND cafe = %s'

    cur.execute(sql, (user_id, user_code, cafe_name))

    conn.commit()
    conn.close()


def getCouponCode(user_id, cafe_name) : # 쿠폰 코드 출력 용

    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '1223334444',
                       db = 'cafewhere_coupon_db',
                       charset = 'utf8')


    cur = conn.cursor()

    sql = "select ifnull(code,0) code from coupon where id = %s AND cafe = %s";
    cur.execute(sql, (user_id, cafe_name))

    ret = cur.fetchone()
    str = ''.join(ret)

    conn.commit()
    conn.close()
    return str
    
    
def getCouponIDCafe(user_id, cafe_name) : # 유저가 쿠폰 뽑았는지 확인 용
    ret = []

    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '1223334444',
                       db = 'cafewhere_coupon_db',
                       charset = 'utf8')


    cur = conn.cursor()

    sql = "select id, cafe from coupon where id = %s AND cafe = %s";
    cur.execute(sql, (user_id, cafe_name))
    
    ret = cur.fetchone()

    conn.commit()
    conn.close()
    if ret == None :
        return 0
    else :
        return 1
    
    
def getCouponCount(cafe_name) : # 특정 카페의 쿠폰 발급 횟수 -> 개수 한정 위해 필요

    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '1223334444',
                       db = 'cafewhere_coupon_db',
                       charset = 'utf8')


    cur = conn.cursor()

    sql = "select count(cafe) from coupon where cafe = %s";
    cur.execute(sql, (cafe_name))
    
    ret = cur.fetchone()

    conn.commit()
    conn.close()
    return ret[0]
    

if __name__ == '__main__' : ## mysql test
    print(getCoupon())
    insCoupon('1111', '2222', '3333')
    print(getCoupon())
    insCoupon(1212, 2323, 3434)
    print(getCoupon())
    insCoupon('1111', '2222', '4444')
    insCoupon('2233', '4545', '4444')
    print(getCoupon())
    print(getCouponCount(4444))
    print(getCouponCode(1111, 3333))
    print(getCode_fordup())
    print(getCouponIDCafe(1111, 3333))
    delCoupon('1111', '2222', '3333')
    print(getCoupon())
    print(getCouponIDCafe(1111, 4444))
    print(getCouponIDCafe(1111, 3333))
    delAll()
    print(getCoupon())
    
