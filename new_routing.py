import random
from interpolate_plotting import*
import re
from flask import Flask,url_for,request,render_template
ctr=0
app=Flask(__name__)
#in url_for name of function comes in form of string
@app.route('/',methods=['GET','POST'])
def hello():
    createLink1="<a href='"+url_for('take')+"'>CALCULATE AVERAGE</a>"
    createLink2="<a href='"+url_for('show')+"'>NUMPY PLOTTING</a>"
    createLink3="<a href='"+url_for('profile_harpreet')+"'>Harpreet Singh</a>"
    createLink4="<a href='"+url_for('profile_shubham')+"'>Shubham Saini</a>"
    createLink5="<a href='"+url_for('profile_vedant')+"'>Vedant Agrawal</a>"
    return """<HTML>
                <head>
                  <title>web assignment</title>
                </head>
                <body bgcolor=#EBD6D6>
                     <div id="title"><marquee><h1>WEB DESIGNING ASSIGNMENT</h1></marquee></div>
                     <div>
                     <h2><i><u>DEVELOPERS</u></i></h2><br>
                     </div>
                     <center><h2>"""+createLink3+"""</h2></center>
                     <center><h2>"""+createLink4+"""</h2></a></center>
                     <center><h2>"""+createLink5+"""</h2></a><br/></center>
                     <center><div>
                     <h2>""" + createLink1 + """</h2></a><br/>
                     <h2>""" + createLink2 + """</h2></a><br/>
                     </div> </center>  
                </body>
                </html>"""
@app.route('/plot',methods=['GET','POST'])
def take():
    if request.method=='GET':
        #send the user the form
        return render_template('calculating_average.html');
    elif request.method=='POST':
        #read form data and save it
        str=request.form['string']
        L=re.split(r'[,]',str)
        L=map(int,L)
        L=list(L)
        av=sum(L)/len(L)
        return render_template('output_average.html',average=av)
        #store data in data store
    else:
        return "<h2>Invalid request</h2>"

@app.route('/make',methods=['GET','POST'])
def show():
    if request.method=='GET':
        #send the user the form
        return render_template('plotting.html');
    elif request.method=='POST':
        render_template('return_plot.html',figure="")
        #read form data and save it
        x_coordinates=request.form['list1']
        y_coordinates=request.form['list2']
        x_coordinates=re.split(r'[,]',x_coordinates)
        y_coordinates=re.split(r'[,]',y_coordinates)
        x_coordinates=map(int,x_coordinates)
        y_coordinates=map(int,y_coordinates)
        x_coordinates=list(x_coordinates)
        y_coordinates=list(y_coordinates)
        ctr=random.randint(0,1000)        
        #algorithm for interpolate
        apx=Interpolate()
        apx.plot(x_coordinates,y_coordinates,ctr)
        str3=apx.Lagrange(x_coordinates,y_coordinates)
        xx='this_plot'+str(ctr)+'.png'                                                          
        return render_template('return_plot.html',figure=url_for('static',filename=xx),poly=str3)
        #store data in data store
    else:
        return "<h2>Invalid request</h2>"
@app.route('/profile1')
def profile_harpreet():
    if request.method=='GET':
        #send the user the form
        return render_template('Harpreet Singh.html',path=url_for('static',filename='profilepic1.jpg'));
@app.route('/profile2')
def profile_shubham():
    if request.method=='GET':
        #send the user the form
        return render_template('Shubham saini.html',path=url_for('static',filename='profilepic2.jpg'));
@app.route('/profile3')
def profile_vedant():
    if request.method=='GET':
        #send the user the form
        return render_template('Vedant agrawal.html',path=url_for('static',filename='profilepic3.jpg'));
      
