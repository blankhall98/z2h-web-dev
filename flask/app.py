# imports
from flask import Flask, render_template, redirect, url_for

# init app
app = Flask(__name__)

# routes

#ruta principal
@app.route('/')
def index():
    return render_template('index.html')

#ruta info
@app.route('/info')
def info():
    return render_template('info.html')

#ruta projects
@app.route('/projects')
def projects():
    return render_template('projects.html')

#run the app
if __name__ == '__main__':
    app.run(debug=True)