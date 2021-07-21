from app import db

subs = db.Table('book to authors',
                db.Column('id', db.Integer, db.ForeignKey('books.id')),
                db.Column('author_id', db.Integer, db.ForeignKey('authors.author_id'))
                )


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), index=True, unique=True)
    author = db.Column(db.String(200), index=True, unique=False)
    status = db.relationship('Status', backref='books', uselist=False)

    def __str__(self):
        return f"<Book: {self.title}>"


class Authors(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=False)
    surname = db.Column(db.String(100), index=True, unique=False)

    def __str__(self):
        return f"<Author: {self.name}>"


class Status(db.Model):
    status_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), index=True, unique=False)
    id = db.Column(db.Integer, db.ForeignKey('books.id'))

    def __str__(self):
        return f"<Status: {self.status}>"
