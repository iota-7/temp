from flask import Flask 

app = Flask(__name__) 

@app.route("/") 
def home_view(): 
		return "<h1>Welcome to Geeks for Geeks</h1>"

# from app.main import app 

if __name__ == "__main__": 
		app.run() 
