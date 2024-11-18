from flask import Blueprint
from flask import render_template

home_bp = Blueprint("home", __name__, url_prefix="/")

@home_bp.get("/")
def home():
    return render_template("home.html")
