from app import create_app
from flask import render_template, jsonify, send_file
from werkzeug.exceptions import HTTPException
from app.exceptions import InputFileProcessingException
import logging
from flask_swagger_ui import get_swaggerui_blueprint


logger = logging.getLogger(__name__)

app = create_app()
@app.route('/')
def home():
    return render_template('index.html')

SWAGGER_URL = '/api/docs' 
API_URL = 'swagger.yaml' 


swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, 
    API_URL,
    config={ 
        'app_name': "Test application"
    }
)

app.register_blueprint(swaggerui_blueprint)

@app.route('/api/docs/swagger.yaml', methods=['GET'])
def swagger():
    return send_file('swagger.yaml')

@app.errorhandler(Exception)
def handle_error(e):
    logger.error(e)
    if isinstance(e, InputFileProcessingException):
        return {"error": str(e)}, 500
    if(isinstance(e, HTTPException)):
        return {"error": "Something went wrong."}, 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')