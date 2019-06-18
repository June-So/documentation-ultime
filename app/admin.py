from app import app, db
from flask import render_template, redirect, url_for, flash
from .forms import CategoryForm, DocumentationForm
from .models import Category, Documentation, Flux, TypeFlux, Tag, User, Section
from flask_user import login_required, UserManager, roles_required

user_manager = UserManager(app, db, User)


@app.route('/register')
def register():
    return render_template('admin/register.html')


@app.route('/admin/', methods=('GET', 'POST'))
@roles_required('Admin')
def add_documentation():
    categorys = Category.query.all()

    form_doc = DocumentationForm.new()
    if form_doc.validate_on_submit():
        # -- add new Documentation
        category = Category.query.get(form_doc.category.data)
        tag = Tag.query.get(form_doc.tag.data)
        new_documentation = Documentation(
                category = category,
                text = form_doc.url_text.data,
                url = form_doc.url.data,
                lang = form_doc.lang.data,
                source = form_doc.source.data,
                tag = tag
            )
        db.session.add(new_documentation)
        db.session.commit()

        type_documentation = TypeFlux.query.filter_by(name='DOCUMENTATION').first()
        new_flux = Flux(type_documentation, new_documentation.id)
        db.session.add(new_flux)
        db.session.commit()
        flash('Documentation ajouté !')
        return redirect(url_for('add_documentation'))

    form_category = CategoryForm.new()
    if form_category.validate_on_submit():
        new_category = Category(form_category.name.data)
        new_category.section = Section.query.get(form_category.section.data)
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('add_documentation'))

    return render_template('admin/index.html', form_category=form_category, form_doc=form_doc, categorys=categorys)


@app.route('/admin/remove-category-<id>')
@roles_required('Admin')
def remove_category(id):
    category = Category.query.get(id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('add_documentation'))



