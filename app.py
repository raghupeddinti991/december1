from flask import Flask, render_template,url_for

app = Flask(__name__)

  

@app.route('/')
@app.route('/basic')
def homepage():
    return render_template('basic.html',title='Git Basic')

 

if __name__ == '__main__':
    app.run(debug=True)