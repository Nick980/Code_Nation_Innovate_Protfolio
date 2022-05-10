from flask import Blueprint, render_template, redirect, request

from favorites import fave_bands, add_to_list, del_from_list

my_view = Blueprint('my_view', __name__)

@my_view.route("/")
def home():
    return render_template("home.html")

@my_view.route("/contact")
def contact():
    return render_template("contact.html")

@my_view.route("/about", methods={"GET", "POST"})
def about():
    if request.method == "POST":
        new_band = request.form["add_band"]
        add_to_list(new_band)
    else:
        remove_band = request.form["remove_band"]
        del_from_list(remove_band)
    return render_template("about.html", bands=fave_bands) 