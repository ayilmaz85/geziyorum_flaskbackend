from flask import Blueprint, jsonify, request
from geziyorum.products import Products


apiProducts = Blueprint("apiProducts", __name__, url_prefix="/api/products")


@apiProducts.route("/")
def products():
    try:
        allProducts = Products.get_all_products()
        allProductsList = []
        for product in allProducts:
            print(product)
            allProductsList.append(
                {
                    "id": product.id,
                    "product_name": product.product_name,

                }
            )
        return jsonify({"success": True, "data": allProductsList, "count": len(allProductsList)})
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": "There is an error..Product doesnt add"})


@apiProducts.route("/addProduct", methods=["POST"])
def addproduct():
    try:
        number = request.form.get("number")

        name = request.form.get("PRODUCT_NAME")

        if name == None:
            return jsonify({"success": False, "message": "Name is required"})

        Products.add_product(number, name)

        return jsonify({"success": True, "message": "Product added successfully"})
    except Exception as e:
        print("ERROR in add_admin: ", e)
        return jsonify({"success": False, "message": "There is an error.."})
