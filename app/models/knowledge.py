from datetime import datetime
from app.extensions import db


class KnowledgeArticle(db.Model):
    """A searchable FAQ / policy entry the AI assistant can draw on."""
    __tablename__ = "knowledge_articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), default="faq")  # faq, policy, document
    keywords = db.Column(db.String(300), default="")  # comma-separated, used for matching
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def keyword_list(self):
        return [k.strip().lower() for k in self.keywords.split(",") if k.strip()]
