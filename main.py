from turtle import title
from flask import *
from requests import post

from DBM import *

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("Home.html")


@app.route("/AuthorRegister")
def areg():
    return render_template("Author_register.html")


@app.route("/UserRegister")
def ureg():
    return render_template("User_register.html")


@app.route("/AuthorLogin")
def alog():
    return render_template("Author_login.html")

@app.route("/UserLogin")
def ulog():
    return render_template("User_login.html")


@app.route("/BlogPost")
def bpost():
    return render_template("Blog_post.html")


@app.route("/ViewPost")
def vpost():
    a=selectAllPost()
    return render_template("View_post.html",elist=a)

#@app.route("/ViewPost")
#def vpost():
#    return render_template("View_post.html")    

@app.route("/Author")
def auth():
    return render_template("Author.html")

@app.route("/User")
def userh():
    return render_template("User.html")

@app.route("/adddata",methods=["post"])
def add():
    name=request.form["Name"]
    email=request.form["Email"]
    password=request.form["Password"]
    city=request.form["City"]
    t=(name,email,password,city)
    addAuthor(t)
    return redirect("/AuthorLogin")

@app.route("/adddata1",methods=["post"])
def add1():
    name=request.form["Name"]
    email=request.form["Email"]
    password=request.form["Password"]
    city=request.form["City"]
    t=(name,email,password,city)
    addUser(t)
    return redirect("/UserLogin")


@app.route("/AuthorLogin",methods=["post"])
def authlog():
    email=request.form["Email"]
    password=request.form["Password"]
    t=(email,password)
    t1=checkalg(t)
    if t in t1:
        return redirect("/Author")
        #return redirect("/ViewPost")
    else:
        return redirect("/AuthorLogin")  



@app.route("/UserLogin",methods=["post"])
def userlog():
    email=request.form["Email"]
    password=request.form["Password"]
    t=(email,password)
    t1=checkulg(t)
    if t in t1:
        return redirect("/User")
    else:
        return redirect("/UserLogin")


@app.route("/blogcheck",methods=["post"])
def addblog2():
    name=request.form["Name"]
    title=request.form["Title"]
    blog=request.form["Post"]
    t=(name,title,blog)
    blogcheck2(t)
    return redirect("/ViewPost")

#@app.route("/adddata4",methods=["post"])
#def add4():
#    name=request.form["Name"]
#    title=request.form["Title"]
#    post=request.form["Post"]
#    t=(name,title,post)
#    addblog(t)
#    return redirect("/ViewPost")    


if __name__=="__main__":
    app.run(debug=True)
