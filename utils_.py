def make_item(cafe_name = f"카페 이름"
            , cafe_address = f"카페 주소"
            , cafe_description = f"보물상자 안에는 뭐가 있을까"
            , cafe_imageUrl = f"https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
            , cafe_webLinkUrl = f"https://e.kakao.com/t/hello-ryan"
            , button = True):


    if button:
        if cafe_description == None:
            cafe_description = cafe_address
            
        item = {
            "title": f"{cafe_name}",
            "description": f"{cafe_description}",
            "thumbnail": {
                "imageUrl": f"{cafe_imageUrl}"
                },
            "buttons": [
                {
                "action":  "webLink",
                "label": "네이버 지도 열기",
                "webLinkUrl": f"{cafe_webLinkUrl}"
                }
                ]
            }
    else:
        item = {
            "title": f"{cafe_name}",
            "description": f"{cafe_description}",
            "thumbnail": {
                "imageUrl": f"{cafe_imageUrl}"
                }
            }
    return item