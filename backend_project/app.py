from flask import Flask, render_template
from views import my_view

app = Flask(__name__)
app.register_blueprint(my_view)

@app.errorhandler(404)                                      #error handling for 404 error, sends user to page and passes the error for the user to see
def page_not_found(e):
    return render_template("404.html", e=e)

if __name__ =="__main__":
    app.run(debug=True, port=8000)