from flask import Flask, escape, request,render_template

#start app
app = Flask(__name__)

#
@app.route('/')
def hello():
    return  render_template ("index.html")


@app.route('/hello')
def dora(): 
    a = request.args.get("a", 0)
    b = request.args.get("b", 0)
    return  render_template ("index.html",a=a,b=b)



@app.route('/rere')
def fefe(): 
    a = request.args.get("a", 0)
    b = request.args.get("b", 0)
    return  render_template ("rere.html",a=a,b=b)


@app.route('/meme')
def ueue(): 
    a = request.args.get("a", 0)
    b = request.args.get("b", 0)
    return  render_template ("meme.html",a=a,b=b)

@app.route('/home')
def home():
    return  render_template ("home.html")

@app.route('/about')
def about():
    return  render_template ("about.html")


@app.route('/picture')
def picture():
    return  render_template ("picture.html")

@app.route('/product')
def product():
    return  render_template ("product.html")
#行事曆
@app.route('/Calendar')
def Calendar():
    return  render_template ("Calendar.html")
    #猜拳
@app.route('/rcp')
def rcp():
    return  render_template ("rcp.html")


@app.route('/*')
def imdex1():
    return  render_template ("index1.html")

@app.route('/2')
def 鬼滅豬認():
    return  render_template ("鬼滅豬認.html")

@app.route('/3')
def 猴跳牆():
    return  render_template ("猴跳牆.html")