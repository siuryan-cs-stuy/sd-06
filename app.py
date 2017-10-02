from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':
        response = request.form['textbox']
    return render_template('index.html', request_method = request.method, response = response)

if __name__ == '__main__':
    app.debug = True
    app.run()
