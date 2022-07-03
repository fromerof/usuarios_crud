from curses import use_default_colors
from flask import Flask, render_template,request,redirect
# importar la clase de friend.py
from users import User
app = Flask(__name__)
@app.route("/")
def index():
    users = User.get_all()
    return render_template("index.html",users=users)
            
@app.route("/user/addUsers")
def addUsers():
    return render_template("addUsers.html")

@app.route("/user/create_user", methods=["POST"]) #######
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect("/")

@app.route("/user/show/<int:id>")
def show(id):
    data = {
        "id":id
    }
    return render_template("infoUser.html",user=User.select(data))

@app.route("/user/edit/<int:id>")
def edit(id):
    data = {
        "id":id
    }
    print("ESTO VA ANTES QUE UPDATE")
    return render_template("edit.html",user=User.select(data))   

@app.route("/user/update", methods=["POST"]) ########
def update():
    print("antes q el error id")
    print(request.form)
    User.update(request.form)
    print("AQUI DEBERIA MODIFICARSE")
    return redirect("/")
    
@app.route("/user/delete/<int:id>")
def delete(id):
    data = {
        "id":id
    }
    User.delete(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)