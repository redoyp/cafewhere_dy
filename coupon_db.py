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

    db.commit()
    db.close()
    return ret


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

    db.commit()
    db.close()
    return ret



def insCoupon(user_id, user_code, cafe_name) : # table에 삽입
    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '1223334444',
                       db = 'cafewhere_coupon_db',
                       charset = 'utf8')


    cur = conn.cursor()

    sql = '''insert into coupon (id, code, cafe) values (%s, %s, %s)'''

    curs.execute(sql, (user_id, user_code, cafe_name))

    db.commit()
    db.close()


def getCouponCode(user_id, cafe_name) : # 쿠폰 코드 출력 용 + 유저가 쿠폰 뽑았는지 확인 용

    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '1223334444',
                       db = 'cafewhere_coupon_db',
                       charset = 'utf8')


    cur = conn.cursor()

    sql = "select ifnull(code,0) code from coupon where id = %s AND cafe = %s";
    cur.execute(sql, (user_id, cafe_name))

    ret = cur.fetchall()

    db.commit()
    db.close()
    return ret


if __name__ == '__main__' : ## coupon code generate test
    coupon_list = getCoupon()
    print(coupon_list)
    
print(getCode_fordup())
