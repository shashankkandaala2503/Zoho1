from flask import Flask,render_template,request
from convert import convert_method,convert_method2,convert_method1


app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def homepage():
	return render_template('home.html')


@app.route("/res",methods=["POST"])
def result():
	text=request.form['address']
	address1,address2= convert_method(text)
	return render_template('res.html',address1= address1,address2=address2)




@app.route("/res1",methods=["POST"])
def result1():
    text1=request.form['address1']
    text2=request.form['address2']

    net_a = convert_method1(text1,text2)
    cidr= convert_method2(text1,text2)
    
    return render_template('res2.html',cidr=cidr,net_a=net_a)





if __name__== '__main__':
	app.run (debug = True)
