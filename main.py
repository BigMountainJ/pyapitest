from app import create_app
from flask import Flask, render_template

app = create_app()
@app.route('/')
def home():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)