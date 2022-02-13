from flask import Flask,redirect,url_for,render_template,request
import random
import os,datetime
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Xeber(db.Model):
    n_id = db.Column(db.Integer, primary_key=True)
    n_img = db.Column(db.String(80))
    n_ad = db.Column(db.String(120))
    n_paragraf = db.Column(db.String(120))
    n_date = db.Column(db.String(120))
    
class Task(db.Model):
    n_id = db.Column(db.Integer, primary_key=True)
    n_date = db.Column(db.String(120))
    n_ixtisas = db.Column(db.String(80))
    n_universtet = db.Column(db.String(120))
    n_haqqinda = db.Column(db.String(120))

class Emr(db.Model):
    n_id = db.Column(db.Integer, primary_key=True)
    n_img = db.Column(db.String(80))
    n_date = db.Column(db.String(120))

class Test(db.Model):
    n_id = db.Column(db.Integer, primary_key=True)
    n_img = db.Column(db.String(80))
    n_ad = db.Column(db.String(120))
    n_adress = db.Column(db.String(120))
    n_paragraf = db.Column(db.String(120))
    n_date = db.Column(db.String(120))
    
# db.create_all()
# class Images:
#     def __init__(self,_id,_src):
#         self.id=_id
#         self.src=_src
# images=[
#       Images(
#             random.randint(1,1000),
#             '../static/image/project-1.jpg'
            
            
#       ),
#       Images(
#             random.randint(1,1000),
#             '../static/image/project-5.jpg'
#       ),
#       Images(
#             random.randint(1,1000),
#             '../static/image/project-3.jpg'
#       ),
#       Images(
#             random.randint(1,1000),
#             '../static/image/project-1.jpg'
#       ),
#       Images(
#             random.randint(1,1000),
#             '../static/image/project-5.jpg'
#       ),
#        Images(
#             random.randint(1,1000),
#             '../static/image/project-3.jpg'
#       ),
# ]

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
# class Comments:
#     def __init__(self,_id,_img,_name,_adress,_paragraf,_icon):
#         self.id=_id
#         self.img=_img
#         self.name=_name
#         self.adress=_adress
#         self.paragraf=_paragraf
#         self.icon=_icon
             
# comments=[
#     Comments(
#         random.randint(1,1000),
#         '../static/image/nurlan1.jpg ',
#         'Dennis Jacques',
#         'User from Baku',
#         'Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam, reprehenderit!',
#         'fas fa-star '
#     )
    
    
    
# ]

     
# @app.route('/',methods=['GET','POST'])
# def hosts(): 
#   return render_template('index.html',allnews=news,allboxs=boxs,allimages=images,allcomments=comments)
  
#  contact sectionun app routu   
@app.route('/',methods=['GET','POST'])
def add():
  butunxeberler=Xeber.query.all()
  butuntasklar=Task.query.all()
  butunemrler=Emr.query.all()
  butuntestler=Test.query.all()
     
        
  return render_template('index.html',xeberler=butunxeberler,tasklar=butuntasklar,emrler=butunemrler,testler=butuntestler)

istifadeciler=[]
@app.route('/users',methods=['GET','POST'])

def users(): 
  if request.method=='POST':
    _ad=request.form['ad']
    _soyad=request.form['soyad']
    _textarea=request.form['textarea']

    istifadeci={
      'ad':_ad,
      'soyad':_soyad, 
      'textarea':_textarea
    }
    istifadeciler.append(istifadeci)
    return render_template('admin.html',users=istifadeciler)
  return render_template('admin.html')
# what I do sectionun app routu
@app.route('/',methods=['GET','POST'])
def app_index():
  butunxeberler=Xeber.query.all()
      
  return render_template('index.html',xeberler=butunxeberler) 
xeberler=[]
@app.route('/admin',methods=['GET','POST'])
def admin_index():
  butunxeberler=Xeber.query.all()  
  if request.method=='POST':
    file=request.files['sekil']
    seklinadi=file.filename
    file.save(os.path.join('static/uploads/',seklinadi))
    _ad=request.form['ad']
    _paragraf=request.form['paragraf']
    _seklinadi=seklinadi
    _tarix=datetime.date.today()
    xeber=Xeber(
        n_img=_seklinadi,
        n_ad=_ad,
        n_paragraf=_paragraf,
        n_date=_tarix
    )
    db.session.add(xeber)
    db.session.commit()
    return redirect('/admin')
  
       
  return render_template('admin.html',xeberler=butunxeberler)      

@app.route('/admin/delete/<id>',methods=['GET','POST'])

def admin_delete(id):
  silinecekolanXeber=Xeber.query.get(id)
  db.session.delete(silinecekolanXeber)
  db.session.commit()
  return redirect('/admin')
#  Resume sectionun app routu
@app.route('/',methods=['GET','POST'])
def app_indexx():
  butuntasklar=Task.query.all()   
  return render_template('index.html',tasklar=butuntasklar) 
Tasklar=[]
@app.route('/nurlan',methods=['GET','POST'])
def admin_indexx():
  
  butuntasklar=Task.query.all()  
  if request.method=='POST':
    _tarix=request.form['date']
    _ixtisas=request.form['ixtisas']
    _universtet=request.form['universtet']
    _haqqinda=request.form['haqqinda']
    
    
   
    task=Task(
        n_date=_tarix,
        n_ixtisas=_ixtisas,
        n_universtet=_universtet,
        n_haqqinda=_haqqinda
       
    )
    db.session.add(task)
    db.session.commit()
    return redirect('/nurlan')
  
       
  return render_template('admin.html',tasklar=butuntasklar)      

@app.route('/nurlan/delete/<id>',methods=['GET','POST'])

def nurlan_delete(id):
  silinecekolanTask=Task.query.get(id)
  db.session.delete(silinecekolanTask)
  db.session.commit()
  return redirect('/nurlan')   
#  portfolo rotunu app routu
@app.route('/',methods=['GET','POST'])
def app_indexxx():
  butunemrler=Emr.query.all()
      
  return render_template('index.html',emrler=butunemrler) 
emrler=[]
@app.route('/cahan',methods=['GET','POST'])
def admin_indexxx():
  butunemrler=Emr.query.all()  
  if request.method=='POST':
    file=request.files["img"]
    seklinadi=file.filename
    file.save(os.path.join('static/uploads/',seklinadi))
    _seklinadi=seklinadi
    _tarix=datetime.date.today()
    emr=Emr(
        n_img=_seklinadi,
        n_date=_tarix
    )
    db.session.add(emr)
    db.session.commit()
    return redirect('/cahan')
  
       
  return render_template('admin.html',emrler=butunemrler)      

@app.route('/cahan/delete/<id>',methods=['GET','POST'])

def cahan_delete(id):
  silinecekolanEmr=Emr.query.get(id)
  db.session.delete(silinecekolanEmr)
  db.session.commit()
  return redirect('/cahan')
# tesmonial routu
@app.route('/',methods=['GET','POST'])
def app_indexxxx():
  butuntestler=Test.query.all()
      
  return render_template('index.html',testler=butuntestler) 
testler=[]
@app.route('/girov',methods=['GET','POST'])
def admin_indexxxx():
  butuntestler=Test.query.all()  
  if request.method=='POST':
    file=request.files["img"]
    seklinadi=file.filename
    file.save(os.path.join('static/uploads/',seklinadi))
    _ad=request.form['ad']
    _adress=request.form['adress']
    _paragraf=request.form['paragraf']
    _seklinadi=seklinadi
    _tarix=datetime.date.today()
    
    test=Test(
        n_img=_seklinadi,
        n_ad=_ad,
        n_adress=_adress,
        n_paragraf=_paragraf,
        n_date=_tarix
    )
    db.session.add(test)
    db.session.commit()
    return redirect('/girov')
  
       
  return render_template('admin.html',testler=butuntestler)      

@app.route('/girov/delete/<id>',methods=['GET','POST'])

def girov_delete(id):
  silinecekolanTest=Test.query.get(id)
  db.session.delete(silinecekolanTest)
  db.session.commit()
  return redirect('/girov') 

if __name__ == "__main__":
    app.run(port=5000,debug=True)
