import random
import coupon
from coupon_db import getCode_fordup

def to_base62(n) :
    codec = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = n % 62
    code = codec[index]
    return code

def code_generate() :
    num = random.randint(1, 62)
    return num

def coupon_code() :
    string = []

    for i in range(12) :
        num = code_generate()
        num = to_base62(num)
        string.append(num)

    return "".join(string)

def coupon_dup() :
    code = coupon_code()
    temp = getCode_fordup()

    if code in temp :
        return coupon_dup()

    return code
