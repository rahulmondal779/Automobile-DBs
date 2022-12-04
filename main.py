from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_manager, login_user, logout_user, login_manager, LoginManager, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# My db connection
local_server = True
app = Flask(__name__)
app.secret_key = '7867'

# Getting unique user access
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# For loading and retrieving users
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Configuration Syntax
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/database_table_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/automobile'
db = SQLAlchemy(app)

# Tables in the sql server are represented as classes, this table is for Login and Register
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(1000))

# Table to store the customer info
class Customer(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=True)
    name = db.Column(db.String(20))
    mobile = db.Column(db.Integer)
    address = db.Column(db.String(1000))
    vehicle_id = db.Column(db.Integer)

# Table to store the customer vehicle
class Customer_vehicle(db.Model):
    cvid = db.Column(db.Integer,primary_key=True)
    vehicle_id = db.Column(db.String(20),unique=True)
    cust_id = db.Column(db.Integer)
    vehicle_name = db.Column(db.String(20))
    model = db.Column(db.String(20))
    color = db.Column(db.String(1000))
    spec = db.Column(db.String(1000))
    num_plate = db.Column(db.String(50))
    warranty = db.Column(db.String(50), nullable=False)
    manufacture_year = db.Column(db.String(50), nullable=False)


# The Home page of the website
@app.route('/')
def index():
    try:
        User.query.all()
        return render_template('index.html')
    except:
        return "Please Connect to Database"

# Register sample
# @app.route("/r")
# def r():
#     return render_template('r.html')

# Customer can login,
@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            # if current_user.email == 'admin@gmail.com':
            #     return redirect(url_for('logs'))
            flash("Login Success", "primary")
            return redirect(url_for('index'))
        else:
            flash("Invalid Credentials", "danger")
            return render_template('login.html')
    return render_template('login.html')


# New Customer can signup, also the password is encrypted when stored in the database
@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        number = request.form.get('number')
        address = request.form.get('address')
        vehicle_id = request.form.get('vehicle_id')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        id = Customer.query.filter_by(vehicle_id=vehicle_id).first()
        if user:
            flash(f"An account with Email {email} already exists", "warning")
            return render_template('/register.html')
        if id:
            flash(f"Vehicle ID {vehicle_id} already exist","warning")
            return render_template('/register.html')
        encpassword = generate_password_hash(password)
        newuser = User(username=username, email=email, password=encpassword)
        db.engine.execute(
            f"INSERT INTO `customer` (`email`,`name`,`mobile`,`address`,`vehicle_id`) VALUES ('{email}','{username}','{number}','{address}','{vehicle_id}') ")
        db.session.add(newuser)
        db.session.commit()
        flash(f"Signup Successful Please Login", "primary")
        return render_template('login.html')
    return render_template('register.html')

# Customer/admin is logged out
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash(f"Logout Successful", "info")
    return redirect(url_for('login'))

# customer details is displayed
@app.route('/customer_details')
@login_required
def c_details():
    log = db.engine.execute(f"SELECT *FROM `user` ")
    em = current_user.email
    query = db.engine.execute(f"SELECT * FROM `customer` WHERE email='{em}'")
    return render_template('c_details.html', query=query)

# To edit details of the customer, 
@app.route("/edit/<string:cid>",methods=['POST', 'GET'])
@login_required
def edit(cid):
    em = current_user.email
    cust = db.engine.execute(f"SELECT *FROM `customer` WHERE email='{em}'")
    posts=Customer.query.filter_by(cid=cid).first()
    if request.method == "POST":
        name = request.form.get('name')
        number = request.form.get('number')
        address = request.form.get('address')
        db.engine.execute(f"UPDATE `customer` SET `name`='{name}',`mobile`='{number}',`address`='{address}' WHERE `customer`.`cid`={cid};")
        print(name)
        flash("Information Updated Successfully", "success")
        return redirect('/customer_details')
    return render_template('c_update.html', posts=posts,cust=cust)

# Shows Customer Vehicle Information 
@app.route("/warranty")
@login_required
def warranty():
    em = current_user.email
    query = db.engine.execute(f"SELECT  *FROM `customer_vehicle` WHERE `customer_vehicle`.`email`='{em}'")
    return render_template('vehicle_info.html',query=query)
    
# Shows the Products which are available,
@app.route('/product')
@login_required
def Product():
    # query = db.engine.execute(f"SELECT *FROM `customer_vehicle`")
    return render_template('product.html')

# Shows Customer the Services we provide to the customer
@app.route('/service')
@login_required
def service():
    return render_template('service.html')

# Contact us Page
@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/test')
def test():
    return render_template('cardstyle.html')

# To run the application
app.run(debug=True)
