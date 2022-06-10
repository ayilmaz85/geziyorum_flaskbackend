from flask import Flask, jsonify, blueprints
from geziyorum import createApp
from geziyorum.initialize_db import createDB
from flask_cors import CORS
from api.users import apiUsers
from api.employees import apiEmployees
from api.products import apiProducts


app = createApp()
CORS(app)
createDB()

app.register_blueprint(apiUsers)
app.register_blueprint(apiEmployees)
app.register_blueprint(apiProducts)
# app.register_blueprint(apiCategories)


@app.route('/')
def index(debug=True):
    return "Hello Flask"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
