from flask import Flask

app=Flask(__name__)



@app.route("/")
@app.route("/home")
def index():
    return "This is the index page"



if __name__ == "__main__":
    app.run(debug=True)
