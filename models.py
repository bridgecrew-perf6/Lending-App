def create_classes(db):
    class Grade(db.Model):
        __tablename__ = 'Grades'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64))
        grade = db.Column(db.Float)
        

        def __repr__(self):
            return '<Grade %r>' % (self.grade)
    return Grade
