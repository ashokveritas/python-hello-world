from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, hello from python flask application!'

@app.route('/health')
def health():
    return 'Hey, health check of the application successfully passed!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
