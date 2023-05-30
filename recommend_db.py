from flask import Flask, request, jsonify
import pymysql

import config as conf
from utils_ import make_item

class recommend_DAO():

    def __init__(self):
        self.conn = None
        

    def connect(self):        
        self.conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '1223334444',
                       db = 'cafewhere_recommend',
                       charset = 'utf8')

    def disconnect(self):
        self.conn.close()


    def make_items(self, address, keyword):
        items = []

        self.connect()
        cur = self.conn.cursor()
            
        sql = f"Select * from CafeKey WHERE dong='{address}' and {keyword}=1 ORDER BY rv_cnt DESC;"
        print(sql)
        #sql = "select id, cafe from coupon where id = %s AND cafe = %s";
        #cur.execute(sql, (address, keyword))
        cur.execute(sql)

        rows = cur.fetchall()
        
        self.conn.commit()
        self.disconnect()


        for i in range(4):
            # name, address, desc, image, web
            if len(rows) > i:
                items.append(make_item(rows[i][3], rows[i][4], rows[i][5], rows[i][6], rows[i][7]))
            else:
                items.append(make_item(f"{len(rows)}, {address} 내에 {keyword} 키워드에 해당하는 카페가 없어요", " ", " ", " ", " ", False))



        return items
