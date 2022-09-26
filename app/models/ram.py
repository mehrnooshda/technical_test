from datetime import datetime

from app import db, ma


class RamUsage(db.Model):
    __tablename__ = 'ram_usage'

    id = db.Column(db.Integer, primary_key=True)
    used = db.Column(db.String(200), unique=False, nullable=True)
    free = db.Column(db.String(512), unique=False, nullable=True)
    total = db.Column(db.String(512), unique=False, nullable=True)

    time = db.Column(db.DateTime, default=datetime.now())


class RamUsageSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = RamUsage

