from my_app import app, session, render_template, request, redirect
from my_app.models.posts import Post

@app.route("/posts/")
def list_posts():
    if "user_logged_in" in session:
        return render_template("posts.html", posts=Post.get_all_posts())

@app.route("/posts/create/", methods=["GET", "POST"])
def create_post():
    if request.method == "GET":
        if "user_logged_in" in session:
            return render_template("create_post.html")
        else:
            return redirect("/user/login/")
    
    else:
        data = {
            "content": request.form["content"],
            "user_id": session["user_logged_in"]
        }
        Post.create_post(data)
        return redirect("/posts/")

@app.route("/posts/delete/", methods=["GET", "POST"])
def delete_post():
    if request.method == "GET":
        return render_template("delete_post.html")
    else:
        data = {
            "post_id": request.form["post_id"]
        }
        Post.delete_post(data)
        return redirect("/posts/")
