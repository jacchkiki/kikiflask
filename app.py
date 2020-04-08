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

