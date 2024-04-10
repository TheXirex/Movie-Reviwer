from os import environ
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.name

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        rating = request.form['rating']

        new_item = Item(name=name, description=description, rating=rating)
        db.session.add(new_item)
        db.session.commit()
        
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/items', methods=['GET'])
def items():
    items = Item.query.all()
    return render_template('items.html', items=items)

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()
    app.run(debug=True)
