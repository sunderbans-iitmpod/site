from flask import Flask
from views import views

app = Flask(__name__)
  
if __name__ == "__main__":
  
	app.register_blueprint(views, url_prefix = "/")
	
	app.run(debug=False, host='0.0.0.0')