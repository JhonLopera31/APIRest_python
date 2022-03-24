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

# product_name as parameter
@app.route('/products/<string:product_name>') #GET is the default method
def get_product(product_name):
    product_match = [
        product for product in products if product["name"] == product_name]
    if len(product_match) > 0:
        return jsonify({"product": product_match[0]})
    else:
        return jsonify({"message": "not found"})
@app.route("/products", methods=["POST"])
def add_product():
    new_product = {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"],
    }
    products.append(new_product)
    return jsonify({"message": "product added", "products": products})


# put se usa para actualizar
@app.route('/products/<string:product_name>', methods=["PUT"])
def edit_product(product_name):
    product_match = [
        product for product in products if product["name"] == product_name]
    if len(product_name) > 0:
        product_match[0]["name"] = request.json["name"]
        product_match[0]["price"] = request.json["price"]
        product_match[0]["quantity"] = request.json["quantity"]

        return jsonify({
            "message": "product updated",
            "product": product_match[0]
        })
    else:
        return "product not found"


@app.route('/products/<string:product_name>', methods=["DELETE"])
def delete_product(product_name):
    product_match = [
        product for product in products if product["name"] == product_name]
    if len(product_match) > 0:
        products.remove(product_match[0])
        return jsonify({
            "message": "product deleted",
            "Updated product list": products
        })
    else:
        return jsonify("Something happend!")

if __name__ == "__main__":
    app.run(debug=True, port=4000)
