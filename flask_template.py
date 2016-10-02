from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "."

@app.route("/second/")
def funct():
	return "second page"

@app.route("/third/")
def funct1():
	return "??"

if __name__ == "__main__":
	app.run()
