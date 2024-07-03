from flask import Flask, jsonify, request #Request proporciona los datos que se le envian por HTTP

app= Flask (__name__)
from products import productos

@app.route ("/Hola")
def ping():
    return jsonify ({"mensaje":"Hola"})

@app.route("/products", methods=["GET"])
def showProducts():
    return jsonify ("Productos: ", productos)

@app.route('/products/<product_name>', methods=["GET"])
def getProduct(product_name):
    for product in productos:
        if product["name"]==product_name:
            productFound= product
    if (len(productFound) > 0):
        return jsonify({'product': productFound[0]})
    return jsonify({'message': 'Product Not found'})

@app.route("/products/post", methods=["POST"]) #BODY, RAW, JSON
def agregarProducto():
    new_product = {
        "name": request.json ["name"],
        "price": request.json ["price"],
        "quantity": request.json ["quantity"]
    }
    productos.append (new_product)
    print (request.json)
    return jsonify("Producto agregado satisfactoriamente", productos)

@app.route ("/products/update/<product_name>", methods= ["PUT"])
def actualizarProductos(product_name):
    for product in productos:
        if product["name"]==product_name:
            productFound= product
        if (len(productFound) > 0):
            productFound[0]["name"] = request.json ["name"]
            productFound [0]["price"] = request.json ["price"]
            productFound[0]["quantity"] = request.json ["quantity"]
            return jsonify ("Producto actualizado." , productFound[0])
    return ("Producto no encontrado.")

@app.route("/products/del/<product_name>", methods= ["DELETE"])
def elimnarProducto(product_name):
    for product in productos:
        if product["name"]==product_name:
            productFound=product
        if len(productFound)>0:
            productos.remove(productFound)
            return jsonify("Producto eliminado.", productos)
        return jsonify ("Producto no encontrado")

if __name__ == "__main__": #Esto va a lo ultimo
    app.run(debug=True)

