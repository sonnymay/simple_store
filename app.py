from flask import Flask, render_template, request

app = Flask(__name__)

# A simple in-memory store for the cart
cart = []

@app.route('/')
def home():
    products = [{'id': 1, 'name': 'Product 1', 'price': 10}, {'id': 2, 'name': 'Product 2', 'price': 20}]
    return render_template('index.html', products=products, cart=cart)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form['product_id']
    cart.append(product_id)
    return 'Product added to cart! <a href="/">Back to home</a>'

if __name__ == '__main__':
    app.run(debug=True)