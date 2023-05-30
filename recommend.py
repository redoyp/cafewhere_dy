# flask import
from flask import Flask, request, jsonify, Blueprint
from recommend_db import *

recommend_server = Blueprint('recommend_server', __name__)

dao = recommend_DAO()


@recommend_server.route('/rec',methods=['POST'])
def rec():
    
    req = request.get_json()
    print(req)

    # TODO: address 입력받기 (action detailParams address value)
    address = req['action']['detailParams']['location']['value']
    keyword = req['action']['clientExtra']['keyword']

    datasend = {
        "version": "2.0",
        "template": {
            "outputs": [
            {
                "carousel": {
                "type": "basicCard",
                "items": dao.make_items(address, keyword)
                }
            }
            ]
        }
    }

    return jsonify(datasend)
