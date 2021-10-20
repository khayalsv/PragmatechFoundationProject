from Project import db

class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, )
    text = db.Column(db.String(50), nullable=False, )
    fb = db.Column(db.String(20),)
    insta = db.Column(db.String(20),)
    twitter = db.Column(db.String(20),)
    image = db.Column(db.String(20),)
    

    def __repr__(self):
        return f'My home: {self.name}'


class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False, )
    image = db.Column(db.String(20),)
    

    def __repr__(self):
        return f'My about: {self.text}'


class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, )
    image = db.Column(db.String(20),)


    def __repr__(self):
        return f'My portfolio: {self.title}'


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, )
    text = db.Column(db.String(250), nullable=False, )
    image = db.Column(db.String(20),)

    def __repr__(self):
          return f'My news: {self.title}'


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, )
    email = db.Column(db.String(100) )
    message = db.Column(db.String(200))
    

    def __repr__(self):
         return f'My contact: {self.name}'
