from app import db
import logging as lg
import pandas as pd
import json

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(42), nullable=False)
    slug = db.Column(db.String(42), nullable=False)
    documentations = db.relationship('Documentation', backref='category', lazy=True)
    concepts = db.relationship('Concept', backref='category', lazy=True)
    faqs = db.relationship('Faq', backref='category', lazy=True)

    def __init__(self, name):
        self.name = name
        self.slug = name.replace(' ', '-').lower()


class Documentation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    lang = db.Column(db.String(12), nullable=True)
    source = db.Column(db.String(60), nullable=True)

    def __init__(self, category, text, url, lang, source):
        self.category = category
        self.text = text
        self.url = url
        self.lang = lang
        self.source = source


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

# -- IMPORT JSON
def db_init(db):
    db.drop_all()
    db.create_all()

    file = open('app/doc/deep_learning.json', encoding='utf-8')
    doc_json = json.load(file)
    for x in doc_json:
        # -- ADD CATEGORY
        category = Category(x['category'])
        db.session.add(category)
        db.session.commit()

        # -- ADD DOCUMENTATIONS
        documentations = [ Documentation(category=category,**doc) for doc in x['documentations'] ]
        for documentation in documentations:
            db.session.add(documentation)
        db.session.commit()

        # -- ADD CONCEPTS
        concepts = [ Concept(category=category,**doc) for doc in x['concepts'] ]
        for concept in concepts:
            db.session.add(concept)
        db.session.commit()

        # -- ADD CONCEPTS
        faqs = [ Faq(category=category,**doc) for doc in x['faq'] ]
        for faq in faqs:
            db.session.add(faq)
        db.session.commit()

    lg.warning('Database initialized')
