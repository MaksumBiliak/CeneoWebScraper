from app import app
from app.forms import ExtractForm
from flask import redirect, render_template, url_for


@app.route("//product/<product_id>")
def product(product_id):
    return render_template("product.html",product_id=product_id)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/extract")
def render_forms():
    form=ExtractForm()
    return render_template("extract.html",form=form)

@app.route("/extract", methods=['POST'])
def extract():
    form=ExtractForm()
    product_id=form.porduct_id
    return redirect(url_for("product",product_id=product_id))