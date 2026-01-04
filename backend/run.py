from flask import Flask, redirect, url_for, render_template
app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/lck")
def LCK():
    return render_template("lck.html")

if __name__ == "__main__":
    app.run(debug=True)