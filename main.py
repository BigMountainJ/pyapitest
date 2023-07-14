from app import create_app
from flask import render_template
from werkzeug.exceptions import HTTPException
from app.exceptions import InputFileProcessingException
import logging

logger = logging.getLogger(__name__)

app = create_app()
@app.route('/')
def home():
    return render_template('index.html')

@app.errorhandler(Exception)
def handle_error(e):
    logger.error(e)
    if isinstance(e, InputFileProcessingException):
        return {"error": str(e)}, 500
    if(isinstance(e, HTTPException)):
        return {"error": "Something went wrong."}, 500
if __name__ == '__main__':
    app.run(host='0.0.0.0')