from flask import Flask,redirect,url_for,render_template,request
import random
app=Flask(__name__)

# class Boxs:
#     def __init__(self,_id,_year,_skill,_universty,_detail):
#         self.id=_id
#         self.year=_year
#         self.skill=_skill
#         self.universty=_universty
#         self.detail=_detail
             
# boxs=[
#     Boxs(
#         random.randint(1,1000),
#         '2015-2019',
#         'Computer Engineer',
#         'Techinal universty',
#         'Lisque persius interesset his et, in quot quidam persequeris vim, ad mea essent possim iriure.'
#     ),
#      Boxs(
#         random.randint(1,1000),
#         '2021-2022',
#         'Web-devoloper',
#         'Pragmatech',
#         'Lisque persius interesset his et, in quot quidam persequeris vim, ad mea essent possim iriure.'
#     ),
     
# ] 
# class News:
#     def __init__(self,_id,_icon,_title,_detail):
#         self.id=_id
#         self.icon=_icon
#         self.title=_title
#         self.detail=_detail
             
# news=[
#     News(
#         random.randint(1,1000),
#         'fab fa-html5',
#         'HTML',
#         'Lisque persius interesset his et, in quot quidam persequeris vim, ad mea essent possim iriure.'
#     ),
#      News(
#         random.randint(1,1000),
#         'fab fa-css3-alt',
#         'CSS',
#         'Lisque persius interesset his et, in quot quidam persequeris vim, ad mea essent possim iriure.'
#     ),
#      News(
#         random.randint(1,1000),
#         'fab fa-bootstrap',
#         'Bootstrap',
#         'Lisque persius interesset his et, in quot quidam persequeris vim, ad mea essent possim iriure.'
#     ),
#      News(
#         random.randint(1,1000),
#         'fab fa-js-square',
#         'Javascript',
#         'Lisque persius interesset his et, in quot quidam persequeris vim, ad mea essent possim iriure.'
#     ),
# ]
userler=[]
@app.route("/",methods=['GET','POST'])
def users(): 
    if request.method=='POST':
        _ad=request.form['ad']
        _soyad=request.form['soyad']
        _textarea=request.form['textarea']

        user={
            'ad':_ad,
            'soyad':_soyad,
            'textarea':_textarea
        }
        userler.append(user)
        return render_template('add.html',istifadeciler=userler)
    return render_template('index.html')
        

    
     

    
if __name__ == '__main__':
    app.run(port=5000,debug=True)