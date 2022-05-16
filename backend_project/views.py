from flask import Blueprint, render_template, redirect, url_for                    #functions imported from flask to allow functionality

my_view = Blueprint('my_view', __name__)                                           #blueprinting for my_view

@my_view.route("/index")                                                           # /, /index, /home redirect to index.html 
@my_view.route("/")                                                                # "/" comes last so page goes to 127.0.0.1:8000 and not 127.0.0.1:8000/index.html
def index():
    return render_template("index.html")

@my_view.route("/admin")                                                           # /admin, /administration redirect to administration.html, not part of navbar, address extension must be entered
@my_view.route("/administration") 
def admin():
    return render_template("administration.html")

@my_view.route("/home")                                                            # /home, /javascript, /js redirect to index.html. Stacked my_view.route for several extensions to simplfy code and avoid repatition
@my_view.route("/javascript")
@my_view.route("/js") 
def index_redirect():
    return redirect(url_for("my_view.index"))

@my_view.route("/page1")                                                           #redirects for additional pages
def page1():
    return render_template("page1.html")

@my_view.route("/page2")
def page2():
    return render_template("page2.html")

@my_view.route("/page3")
def page3():
    return render_template("page3.html")

@my_view.route("/page4")
def page4():
    return render_template("page4.html")

@my_view.route("/page5")
def page5():
    return render_template("page5.html")