from app import app
from app.models import Section

# - JINJA : Return class from review label
@app.context_processor
def to_template():
    def get_sections():
        return Section.query.all()
    return dict(get_sections=get_sections)