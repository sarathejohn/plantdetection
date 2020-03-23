from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
zimport cv2
app = Flask(__name__)
CORS(app) # needed for cross-domain requests, allow everything by default
@app.route('/')
def index():
    img=cv2.imread('abc.png')
    new_model = tf.keras.models.load_model('first.model')
    return 'hi'
  
# HTTP Errors handlers
@app.errorhandler(404)
def url_error(e):
    return """
    Wrong URL!
    <pre>{}</pre>""".format(e), 404

@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500
@app.route('/try')
def hi():
    return render_template('hi.html')
@app.route('/try1',methods = ['POST'])
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
          
        return render_template("hi.html", name = f.filename)  
  
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
