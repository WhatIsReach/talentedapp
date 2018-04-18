from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/upload.html')
def upload():
    return render_template('upload.html')
@app.route('/logged.php')
def logged():
    return render_template('logged.php')


if __name__ == '__main__':
    app.run(debug=True)
