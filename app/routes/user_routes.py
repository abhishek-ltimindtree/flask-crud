from flask import Blueprint, render_template, request, redirect, url_for
from app.services.user_service import *

user_bp = Blueprint("users", __name__)


@user_bp.route("/")
def index():

    users = get_all_users()

    return render_template("users.html", users=users)


@user_bp.route("/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":

        name = request.form["name"]

        email = request.form["email"]

        create_user(name, email)

        return redirect(url_for("users.index"))

    return render_template("user_form.html")


@user_bp.route("/edit/<int:user_id>", methods=["GET", "POST"])
def edit(user_id):

    user = get_user(user_id)

    if request.method == "POST":

        name = request.form["name"]

        email = request.form["email"]

        update_user(user, name, email)

        return redirect(url_for("users.index"))

    return render_template("user_form.html", user=user)


@user_bp.route("/delete/<int:user_id>")
def delete(user_id):

    user = get_user(user_id)

    delete_user(user)

    return redirect(url_for("users.index"))