from app import db
import logging as lg


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


def db_init():
    db.drop_all()
    db.create_all()

    cat_cnn = Category('Convolutional Neural Network')
    cat_series_temp = Category('Série temporelle')
    cat_flask = Category('Flask')
    cat_regex = Category('Regex')
    cat_bdd = Category('Base de données')
    cat_python = Category('Python')
    cat_practice = Category('Pratiquer')


    # db.session.add(Documentation(category=, text='', lang='', source='', url=''))
    # db.session.add(Concept(category=, name="", explain=))

    # -- CNN
    db.session.add(Documentation(category=cat_cnn, text='Comment les Réseaux de neurones à convolution fonctionnent', lang='FR', source='Medium @Charles Crouspeyre', url='https://medium.com/@CharlesCrouspeyre/comment-les-r%C3%A9seaux-de-neurones-%C3%A0-convolution-fonctionnent-b288519dbcf8'))
    db.session.add(Documentation(category=cat_cnn, text='Visualiser les couches', lang='EN', source='Code A Star', url='https://www.codeastar.com/visualize-convolutional-neural-network/'))
    db.session.add(Documentation(category=cat_cnn, text='Charger des images avec Keras', lang="EN", source="Machine Learning Mastery", url="https://machinelearningmastery.com/how-to-load-convert-and-save-images-with-the-keras-api/"))
    db.session.add(Concept(category=cat_cnn, name='Convolution'))
    db.session.add(Concept(category=cat_cnn, name='Pooling'))
    db.session.add(Concept(category=cat_cnn, name='Filtre'))

    # -- Series temporelle
    db.session.add(Documentation(category=cat_series_temp, text="Séries temporelles", lang='FR',source="Xavier Dupre", url="http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/notebooks/_gs2a_timeseries.html"))
    db.session.add(Documentation(category=cat_series_temp, text='Détails série temporelle', lang='FR', source='math u-psud', url='https://www.math.u-psud.fr/~goude/Materials/ProjetMLF/time_series.html'))
    db.session.add(Concept(category=cat_series_temp, name="Persistence", explain="par exemple quand la météo du lendemain est identique à celle du jour"))
    db.session.add(Concept(category=cat_series_temp, name="techniques temporelles déterministes", explain="""L’analyse fréquentielle d’une série temporelle : un signal est approché par une
    somme de sinusoı̈dales (analyse de Fourier).\n

    La décomposition d’une série temporelle en composantes tendancielle, cyclique,
    saisonnière et accidentelle.\n

    La correction des variations saisonnières d’une série temporelle, qu’on étudiera,
    repose sur cette décomposition."""))

    # -- Flask
    db.session.add(Documentation(category=cat_flask, text='The Flask Mega-Tutorial', lang='EN',source='Blog - Miguel Grinberg', url='https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world'))
    db.session.add(Documentation(category=cat_flask, text='Tuto: Concevez un site avec Flask', lang='FR',source='Openclassroom', url='https://openclassrooms.com/fr/courses/4425066-concevez-un-site-avec-flask'))
    db.session.add(Documentation(category=cat_flask, text='Documentation Flask-sqlAlchemy', lang='EN',source='Documentation Officielle', url='http://flask-sqlalchemy.pocoo.org/2.3/'))
    db.session.add(Documentation(category=cat_flask, text='Documentation Flask-sqlAlchemy à sauvegarder en local', lang='EN', source='PDF Documentation Officielle', url='https://media.readthedocs.org/pdf/flask-sqlalchemy/stable/flask-sqlalchemy.pdf'))
    db.session.add(Faq(category=cat_flask,question="Mes images ne s'affichent pas.", answer="Vérifiez que le chemin qui mène à vos images: Allez sur la page contenant les images que vous souhaitez afficher. Faites un CTRL+U et localiser vos balises <img >, le chemin de l'attribut href doit correspondre à l'emplacement de votre fichier. Cliquez sur le lien pour voir le chemin complet apparaître dans la barre d'url. L'adresse de votre serveur [http://127.0.0.1:5000/] est égal à [C:/Chemin/jusquau/dossier/racine/de/votre/projet]. Attention flask ne prend pas les chemin absolu ou relatif, vous devez passez par la fonction url_for() pour cela."))

    # -- Base de données
    db.session.add(Documentation(category=cat_bdd, text='sqlAlchemy - Mapper ses classes', lang="EN",source="Documentation officielle", url="https://docs.sqlalchemy.org/en/latest/orm/tutorial.html"))
    db.session.add(Concept(category=cat_bdd, name='Jointures'))
    db.session.add(Concept(category=cat_bdd, name='Clé étrangère'))

    # -- Regex
    db.session.add(Documentation(category=cat_regex, text='Aide à la création de regex', lang='EN', source='Outils avec documentation', url='https://regex101.com/'))

    # -- Practice
    db.session.add(Documentation(category=cat_practice, text='Cours et entrainements', lang='EN', source='SuperDataScience', url='https://www.superdatascience.com/'))


    db.session.commit()
    lg.warning('Database initialized')
