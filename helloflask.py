# imports
from flask import Flask
 
# run the app
app = Flask(__name__)
 
# route for domain
@app.route("/")
# route function (get)
def hello():
    return "Hello World!"
 
# main (runs python file)
if __name__ == "__main__":
    app.run()