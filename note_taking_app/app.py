from flask import Flask,render_template,request,url_for
from werkzeug.utils import redirect

app = Flask(__name__)

notes = []

@app.route("/",methods = ['GET','POST'])
def index():
    if request.method == "POST":
        n = request.form["n"]
        if len(n) >0 and n not in notes: #not add something more than one time 
            notes.append(n)

    
    return render_template('home.html',notes=notes)

@app.route("/delete/<note>")
def delete(note):
    notes.remove(note)
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run()