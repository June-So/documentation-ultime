from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from .models import Category, Tag


class CategoryForm(Form):
    name = StringField('catégorie', validators=[DataRequired()])
    submit = SubmitField('Enregistrer')


class DocumentationForm(Form):
    category_choices = [(category.id, category.name) for category in Category.query.order_by('name')]
    lang_choices = [('EN', 'EN'), ('FR', 'FR'), ('MULTI', 'MULTI')]
    tag_choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]
    category = SelectField('catégorie', choices=category_choices, coerce=int)
    lang = SelectField('langue', choices=lang_choices)
    url = StringField('url', validators=[DataRequired()])
    url_text = StringField('url_text', validators=[DataRequired()])
    source = StringField('source', validators=[DataRequired()])
    tag = SelectField('tag', choices=tag_choices, coerce=int)
    submit = SubmitField('Enregistrer')
