# coding: utf-8
from flask import redirect, render_template

from . import app

from .auth import logged_in

@app.route("/")
def index():
    if not logged_in():
        return redirect("/login")
    return render_template("InterfaceWEBMAIN.html")
    