from flask import Flask, jsonify, request, session
from flask_mail import Mail, Message
from flask_cors import CORS ,cross_origin

app = Flask(__name__)

app.config['SECRET_KEY'] = 'shut the fuck up'
app.config['CORS_ALLOW_HEADERS'] = 'Content-Type'
#cors
cors = CORS(app, resource={r"/foo": {"origins": "*"}})


mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'kevinosmol7690@gmail.com',
    "MAIL_PASSWORD":'crave654'
}
app.config.update(mail_settings)
mail = Mail(app)

@app.route("/", methods=["GET"])
def home():
    return "WELCOME!!!"

    
@app.route('/api/v1/post-message',  methods = ["POST"])
@cross_origin(origin = '*', headers=['Content- Type', 'Authorization'])
def  index():
    try:
        _email = request.json['email']
        _name = request.json['name']
        _message = request.json['message']

        msg = Message(subject=_name,
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["gassafuah@gmail.com"], 
                      body=" name : "+_name+ "\n email : "+_email+ "\n message : " +_message )
        mail.send(msg)
        return jsonify({"message":"Message sent successfully","status":200})

			
    except Exception as e:
        return jsonify({"message":"Not sent", "status":400})

@app.after_request
def after_request(response):
  #response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response;
   
if  __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
    
    