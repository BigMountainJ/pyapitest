from app import create_app
from flask import render_template, jsonify
from werkzeug.exceptions import HTTPException
from app.exceptions import InputFileProcessingException
import logging
from flask_swagger_ui import get_swaggerui_blueprint

logger = logging.getLogger(__name__)

app = create_app()
@app.route('/')
def home():
    return render_template('index.html')

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'swagger.yaml'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    }
)

app.register_blueprint(swaggerui_blueprint)

@app.errorhandler(Exception)
def handle_error(e):
    logger.error(e)
    if isinstance(e, InputFileProcessingException):
        return {"error": str(e)}, 500
    if(isinstance(e, HTTPException)):
        return {"error": "Something went wrong."}, 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')