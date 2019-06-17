from app import db
import logging as lg
import json
import datetime
from flask_user import UserMixin


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(42), nullable=False, unique=True)
    slug = db.Column(db.String(42), nullable=False)
    categorys = db.relationship('Category', backref='section', lazy=True)

    def __init__(self, name, slug):
        self.name = name
        self.slug = slug



class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(42), nullable=False, unique=True)
    slug = db.Column(db.String(42), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=True)
    documentations = db.relationship('Documentation', backref='category', lazy=True)
    concepts = db.relationship('Concept', backref='category', lazy=True)
    faqs = db.relationship('Faq', backref='category', lazy=True)

    def __init__(self, name):
        self.name = name
        self.slug = name.replace(' ', '-').lower()


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    i_class = db.Column(db.String(255), nullable=False)
    documentations = db.relationship('Documentation', backref='tag', lazy=True)

    def __init__(self, name, i_class):
        self.name = name
        self.i_class = i_class


class Documentation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=True)
    url = db.Column(db.String(255), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    lang = db.Column(db.String(12), nullable=True)
    source = db.Column(db.String(255), nullable=True)

    def __init__(self, category, text, url, lang, source, tag):
        self.category = category
        self.text = text
        self.url = url
        self.lang = lang
        self.source = source
        self.tag = tag


class Concept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    name = db.Column(db.String(42), nullable=False)
    explain = db.Column(db.Text, nullable=True)

    def __init__(self, name, category, explain=''):
        self.name = name
        self.category = category
        self.explain = explain


class Faq(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.Text, nullable=True)

    def __init__(self, category, question, answer=''):
        self.category = category
        self.question = question
        self.answer = answer


class Flux(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_create = db.Column(db.DateTime, nullable=False)
    type_flux_id = db.Column(db.Integer, db.ForeignKey('type_flux.id'), nullable=False)
    objet_id = db.Column(db.Integer, nullable=False)

    def __init__(self, type_flux, objet_id):
        self.date_create = datetime.datetime.now()
        self.type_flux = type_flux
        self.objet_id = objet_id


class TypeFlux(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    fluxs = db.relationship('Flux', backref='type_flux', lazy=True)

    def __init__(self, name, i_class):
        self.name = name
        self.i_class = i_class


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    # User authentication information. The collation='NOCASE' is required
    # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    roles = db.relationship('Role', secondary='user_roles')
    email_confirmed_at = db.Column(db.DateTime())

# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

