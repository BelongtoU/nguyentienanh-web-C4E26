from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

all_clt = MongoClient(uri).c4e 

posts_clt = all_clt["posts"]

new_post ={
    "title": "HELP ME :((",
    "author": "Tien Anh Nguyen C4E26",
    "content": """
                Ae cíuuuuu :((
                T vẫn ko biết đăng nhập vào cái trình duyệt của db như nào :(( ngồi cả sáng r :(( 
                Someone ngang qua đây có thấy thì chỉ mình vs :(( mình cảm ơn <3 
                FB: https://www.facebook.com/caube.gio.739
    """
}

posts_clt.delete_one(new_post)
