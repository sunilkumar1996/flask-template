from flask import Flask, render_template, request, redirect, url_for
import pdb
import json
# import pysqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# Database conection here with sqlite3
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////home/sunilrajput/workspace/python/Flask-with-template/product.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Create model
class Product(db.Model):
	__tablename__ = "products"
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50), nullable=False)
	price = db.Column(db.Float, nullable=False)
	description = db.Column(db.String(50), nullable=False)

	# Reprent String record
	def __str__(self, title, price, description):
		self.title = title
		self.price = price
		self.description = description

	# Insert New Record here ...
	def add_product(_title, _price, _description):
		new_rec = Product(title=_title, price=_price, description=_description)
		db.session.add(new_rec)
		db.session.commit()

	# Reprasent required record here...
	def __repr__(self):
		object_all = {
		'id': self.id,
		'title': self.title,
		'price': self.price,
		'description': self.description
		}
		return json.dumps(object_all)

# Home route
@app.route("/")
def home():
	product = Product.query.all()
	return render_template("home.html", product=product)

# New Record add route here
@app.route('/item/new', methods=['POST', 'GET'])
def new_item():
	# pdb.set_trace()
	# New Record Add in database..
	if request.method == "POST":
		title = request.form.get('title')
		price = request.form.get('price')
		description = request.form.get('description')
		data = Product(title=title, price=price, description=description)
		db.session.add(data)
		db.session.commit()
		# Process the form data
		# print("Form Data: ")
		# print("title: {}, description: {}".format(request.form.get('title'),request.form.get('price'), request.form.get('description')))
		# Redirect to some page..
		return redirect(url_for('home'))
	return render_template("new_item.html")

# App Run and debug always true and debug use this mode
if __name__=="__main__":
	app.run(debug=True)
