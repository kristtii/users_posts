from my_app import app, session, render_template, redirect, request
from my_app.models.users import User

@app.route("/user/")
def users():
	if "user_logged_in" in session:
		return render_template('users.html', users=User.get_all())
	return redirect("/user/login/")

@app.route("/user/login/", methods=["GET", "POST"])
def login():
	if request.method == "GET":
		if "user_logged_in" in session:
			return redirect("/user/")
		return render_template("login.html")
	
	user_data = {
		"email": request.form["email"]
	}
	# Ose do me ktheje None, ose do te ktheje User
	my_user_object = User.get_my_user(user_data)
	if my_user_object is not None:
		session["user_logged_in"] = my_user_object.id
		return redirect("/user/")
	else:
		return render_template("login.html", error_message="Wrong credentials")

@app.route("/user/create/", methods=["GET", "POST"])
def create_user():
	if request.method == "GET":
		return render_template("register.html")	
	
	data = {
		"email": request.form["email"],
		"name": request.form["name"]
	}

	my_user_id = User.create_user(data)

	session["user_logged_in"] = my_user_id

	return redirect("/user/")

@app.route("/user/logout/", methods=["POST"])
def logout():
	session.pop("user_logged_in")
	return redirect("/user/login/")


# @app.route("/user/update")
# @app.route("/user/delete")