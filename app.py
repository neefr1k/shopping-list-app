from flask import Flask, render_template, request, redirect
from database import get_items, add_item, remove_item

app = Flask(__name__)

@app.route("/")
def index():
    items = get_items()
    return render_template("index.html", items=items)

@app.route("/add", methods=["POST"])
def add():
    item = request.form.get("item")
    if item:
        add_item(item)
    return redirect("/")

@app.route("/remove/<item>")
def remove(item):
    remove_item(item)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)