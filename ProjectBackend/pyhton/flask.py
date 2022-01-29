from  flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world"py

if __name__ == '__main__':
    flask.run()
    