from flask import Flask,redirect,url_for,render_template,request
import random

app=Flask(__name__)
class News:
    def __init__(self,_id,_title,_img,_shortinfo,_detail):
        self.id=_id
        self.title=_title
        self.img=_img
        self.shortinfo=_shortinfo
        self.detail=_detail 

news = [
    News(
        random.randint(1,1000),
        'First News title',
        'https://upload.wikimedia.org/wikipedia/tr/0/02/The_Witcher_afi%C5%9F.jpg',
        'short info about',
        'deatil about first news'
  
    ),
     News(
        random.randint(1,1000),
        'First News title',
        'https://upload.wikimedia.org/wikipedia/tr/0/02/The_Witcher_afi%C5%9F.jpg',
        'short info about',
        'deatil about first news'
  
    ),
      News(
        random.randint(1,1000),
        'First News title',
        'https://upload.wikimedia.org/wikipedia/tr/0/02/The_Witcher_afi%C5%9F.jpg',
        'short info about',
        'deatil about first news'
  
    ),
]    

@app.route('/')
def home():
    return render_template('index.html',allnews=news)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)