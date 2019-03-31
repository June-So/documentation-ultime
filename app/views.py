from app import app
from flask import render_template
from app.models import Documentation, Category


@app.route('/')
def documentation():
    categorys = Category.query.all()
    print(categorys)
    return render_template('documentation.html', categorys=categorys)


@app.route('/<category>')
def focus(category):
    category = Category.query.filter_by(slug=category).first()
    return render_template('category.html', category=category)
