from flask import Blueprint, request, send_file
from .services import process_csv
from .utils import validate_csv

api = Blueprint('api', __name__)

@api.route('/process', methods=['POST']) 
def process():
    if not validate_csv(request.files['file']):
        return {"error": "Invalid CSV file"}, 400
    output = process_csv(request.files['file'])
    return send_file(output, mimetype='text/csv', as_attachment=True, download_name='output.csv')