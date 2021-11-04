from quickkart_api import app
from flask import jsonify

@app.errorhandler(404)
def error_404(error):
    return jsonify(error.description), 404

@app.errorhandler(500)
def error_500(error):
    return jsonify(error.description), 404