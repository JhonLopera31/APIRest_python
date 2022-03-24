from products import products
from flask import Flask, jsonify, request

# request is usefull to data from a client
app = Flask(__name__)  # use the server name


@app.route('/test') #Defining a route for testing connection
def ping():
    return jsonify({"message": "Test happening"}) 


@app.route('/products', methods=["GET"])
def get_Products():
    return jsonify({"products": products, "message": "List of products"}) #list all data in producst file


if __name__ == "__main__":
    app.run(debug=True, port=4000)
