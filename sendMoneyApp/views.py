from flask import request, Flask
import pymongo

app = Flask(__name__)


#to have access to vars on config file
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

#connect my DB to my app
try:
    mongo = pymongo.MongoClient(
        host = "localhost",
        port = 27017,
        serverSelectionTimeoutMS = 1
    )
    mongo.server_info() # trigger exception if cannot connect to my DB 
except : 
    print("ERROR - Cannot connect to db")

@app.route('/registration', methods = ['GET', 'POST'])
def register_page():
    if request.method == "GET":
        return "Registration Page"
    elif request.method == "POST":
        pass #logic for adding a new user
    

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == "GET":
        return 'login Page'
    elif request.method == "POST":
        pass #logic for a user signIn (return redirect('listUsers Page' or 'profile Page'))

@app.route('/profile')
def profile_Page():
    return 'Profile page'

@app.route('/')
@app.route('/list-users')
def listUsers ():
    #need cnx with DB to get all registered user
    return 'list-users Page'

@app.route('/show-user-profile/<id>/')
def profile_user(id):
    return id


if __name__ == "__main__":
    app.run()






# @app.route("/user/<id>")
# def user_profile(id):
#     user = mongo.db.users.find_one_or_404({"_id": username})
#     return render_template("user.html",
#         user=user)