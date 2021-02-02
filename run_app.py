from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
import logging
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
ma = Marshmallow(app)
db = SQLAlchemy(app)

logger = logging.getLogger('Quote logger')
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "author", "quote", "date")

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

class QuotesDB(db.Model):

    __tablename__ = 'quotes'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    quote = db.Column(db.String(300), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Quotes %r>' % self.id

class Quote(Resource):

    def get(self):
        quotes = QuotesDB.query.all()
        logging.debug('Show all quotes')
        return posts_schema.dump(quotes)

    def post(self):
        try:
            new_quote = QuotesDB(
            author=request.json['author'],
            quote=request.json['quote'])
        except:
            logging.exception("Author and quote should be mandatory !", request.json)
        db.session.add(new_quote)
        db.session.commit()
        logging.debug('Quotes add to DB')
        return post_schema.dump(new_quote)

    def put(self, id):
        post = QuotesDB.query.get_or_404(id)
        if 'author' in request.json:
            post.author = request.json['author']
        if 'quote' in request.json:
            post.quote = request.json['quote']
        db.session.commit()
        return post_schema.dump(post)

    def delete(self, id):
        post = QuotesDB.query.get_or_404(id)
        local_object = db.session.merge(post)
        db.session.delete(local_object)
        db.session.commit()
        logging.debug('Delete quote with id ' + id)
        return '', 204

@app.route('/')
def hello():
    return 'Hello from Flask!'

api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<string:id>")
if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', debug=True)
