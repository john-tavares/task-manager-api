from datetime import datetime
from database import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    done = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<Task {self.id}>'

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def create(cls, title, description=None):
        task = cls(title=title, description=description)
        db.session.add(task)
        db.session.commit()
        return task

    def update(self, title=None, description=None, done=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if done is not None:
            self.done = done
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': self.done,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }