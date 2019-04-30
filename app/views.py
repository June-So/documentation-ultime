from app import app
from flask import render_template
from app.models import Documentation, Category, Flux


@app.route('/')
def documentation():
    categorys = Category.query.all()
    return render_template('documentation.html', categorys=categorys)


@app.route('/flux')
def flux():
    news = Flux.query.order_by('date_create').all()
    return render_template('flux.html', news=news)


@app.context_processor
def utility_processor():
    def get_documentation(id):
        documentation = Documentation.query.get(id)
        print(documentation)
        return documentation
    return dict(get_documentation=get_documentation)


@app.route('/focus-<category>')
def focus(category):
    category = Category.query.filter_by(slug=category).first()
    return render_template('category.html', category=category)