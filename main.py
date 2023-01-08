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
    cvid = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.String(20), unique=True)
    cust_id = db.Column(db.Integer)
    vehicle_name = db.Column(db.String(20))
    model = db.Column(db.String(20))
    about = db.Column(db.String(20000))
    color = db.Column(db.String(1000))
    spec = db.Column(db.String(1000))
    num_plate = db.Column(db.String(50))
    warranty = db.Column(db.String(50), nullable=False)
    manufacture_year = db.Column(db.String(50), nullable=False)

# Table to Store the customer service vehicle
class Customer_vehicle_service(db.Model):
    cvs_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20))
    description = db.Column(db.String(1000))
    manufacture = db.Column(db.String(50), nullable=False)
    exp_date = db.Column(db.String(50), nullable=False)
    textarea = db.Column(db.String(1000))
    status = db.Column(db.String(10))

# Service Name
class Services(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    services_name = db.Column(db.String(100))


# The Home page of the website
@app.route('/')
def index():
    try:
        User.query.all()
        return render_template('index.html')
    except:
        return "Please Connect To DATABASE"

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
            flash(f"Vehicle ID {vehicle_id} already exist", "warning")
            return render_template('/register.html')
        encpassword = generate_password_hash(password)
        newuser = User(username=username, email=email, password=encpassword)
        db.engine.execute(f"INSERT INTO `customer` (`email`,`name`,`mobile`,`address`,`vehicle_id`) VALUES ('{email}','{username}','{number}','{address}','{vehicle_id}') ")
        db.session.add(newuser)
        db.session.commit()
        flash(f"Signup Successful Please Login", "primary")
        return render_template('login.html')
    return render_template('register.html')

# add new vehicle
@app.route('/add_vehicle', methods=['POST','GET'])
@login_required
def add_vehicle():
    em = current_user.email
    query = db.engine.execute(f"SELECT *FROM `customer` WHERE `customer`.`email`='{em}'")
    if request.method == "POST":
        vehicle_id = request.form.get('vehicle_id')
        email = current_user.email
        vehicle_name = request.form.get('vehicle_name')
        model = request.form.get('model')
        about = request.form.get('about')
        color = request.form.get('color')
        specs = request.form.get('specs')
        numplate = request.form.get('num_plate')
        warrenty = request.form.get('warrenty')
        manudate = request.form.get('manudate')
        db.engine.execute(f"INSERT INTO `customer_vehicle` (`vehicle_id`,`email`,`vehicle_name`,`model`,`About`,`color`,`spec`,`num_plate`,`warranty`,`manufacture_year`) VALUES ('{vehicle_id}','{email}','{vehicle_name}','{model}','{about}','{color}','{specs}','{numplate}','{warrenty}','{manudate}')")
        flash("Vehicle Added Successfully","success")
    return render_template('add_vehicle.html', query=query)

# Shows Customer the Services we provide to the customer
@app.route('/service', methods=['POST', 'GET'])
@login_required
def service():
    em = current_user.email
    query = db.engine.execute(
        f"SELECT `vehicle_id` FROM `customer` WHERE `customer`.`email`='{em}'")
    number_plate = db.engine.execute(
        f"SELECT `num_plate` FROM `customer_vehicle` WHERE `customer_vehicle`.`email`='{em}'")
    services = db.engine.execute(f"SELECT `services_name` FROM `services`")
    if request.method == "POST":
        name = request.form.get('name')
        email = current_user.email
        vehicle_id = request.form.get('Vid')
        num_plate = request.form.get('number_plate')
        service = request.form.get('service')
        manufacture_date = request.form.get('manudate')
        expire_date = request.form.get('expdate')
        issues = request.form.get('issues')
        status = 'Pending'
        flash(f"Booking Confirmed", "success")
        db.engine.execute(f"INSERT INTO `customer_vehicle_service` (`name`,`email`,`vehicle_id`,`num_plate`,`description`,`manufacture`,`exp_date`,`textarea`,`status`) VALUES ('{name}','{email}','{vehicle_id}','{num_plate}','{service}','{manufacture_date}','{expire_date}','{issues}','{status}') ")
    return render_template('service.html', services=services, query=query, number_plate=number_plate)

# This is Booking Page
@app.route('/booking')
@login_required
def booking():
    em = current_user.email
    query = db.engine.execute(f"SELECT *FROM `customer_vehicle_service` WHERE `customer_vehicle_service`.`email`='{em}'")
    return render_template('booking.html', query=query)

# customer details is displayed
@app.route('/customer_details')
@login_required
def c_details():
    log = db.engine.execute(f"SELECT *FROM `user` ")
    em = current_user.email
    query = db.engine.execute(f"SELECT * FROM `customer` WHERE email='{em}'")
    return render_template('c_details.html', query=query)

# To edit details of the customer,
@app.route("/edit/<string:cid>", methods=['POST', 'GET'])
@login_required
def edit(cid):
    em = current_user.email
    cust = db.engine.execute(f"SELECT *FROM `customer` WHERE email='{em}'")
    posts = Customer.query.filter_by(cid=cid).first()
    if request.method == "POST":
        name = request.form.get('name')
        number = request.form.get('number')
        address = request.form.get('address')
        db.engine.execute(f"UPDATE `customer` SET `name`='{name}',`mobile`='{number}',`address`='{address}' WHERE `customer`.`cid`={cid};")
        flash("Information Updated Successfully", "success")
        return redirect('/customer_details')
    return render_template('c_update.html', posts=posts, cust=cust)

# Editing Booking Page
@app.route("/edit-booking/<string:cvs_id>", methods=['POST', 'GET'])
@login_required
def edit_booking(cvs_id):
    em = current_user.email
    query = db.engine.execute(f"SELECT *FROM `customer_vehicle_service` WHERE `customer_vehicle_service`.`email`='{em}'")
    posts = Customer_vehicle_service.query.filter_by(cvs_id=cvs_id).first()
    if request.method == "POST":
        status = request.form.get('status')
        db.engine.execute(f"UPDATE `customer_vehicle_service` SET `status`='{status}' WHERE `customer_vehicle_service`.`cvs_id`={cvs_id};")
        flash("Status Updated Successfully", "success")
        return redirect('/booking')
    return render_template('edit_booking.html', query=query)

# Editing Vehicle Present in the database
@app.route("/edit-vehicle/<string:cvid>",methods=['POST','GET'])
@login_required
def edit_vehicle(cvid):
    em = current_user.email
    query = db.engine.execute(f"SELECT *FROM `customer_vehicle` WHERE `customer_vehicle`.`email`='{em}'")
    posts = db.engine.execute(f"SELECT *FROM `customer_vehicle` WHERE `customer_vehicle`.`cvid`='{cvid}'")
    if request.method == "POST":
        vehicle_id = request.form.get('vehicle_id')
        email = current_user.email
        vehicle_name = request.form.get('vehicle_name')
        model = request.form.get('model')
        about = request.form.get('about')
        color = request.form.get('color')
        specs = request.form.get('specs')
        numplate = request.form.get('num_plate')
        warrenty = request.form.get('warrenty')
        manudate = request.form.get('manudate') 
        db.engine.execute(f"UPDATE `customer_vehicle` SET `vehicle_name`='{vehicle_name}',`model`='{model}',`about`='{about},`color`='{color}',`specs`='{specs}',`num_plate`='{numplate}',`warranty`='{warrenty}',`manufacture_year`='{manudate}'")
        return redirect('/warranty')
    return render_template('vehicle_update.html',query=query,posts=posts)
        

# Customer/admin is logged out
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash(f"Logout Successful", "info")
    return redirect(url_for('login'))

# Shows Customer Vehicle Information
@app.route("/warranty")
@login_required
def warranty():
    em = current_user.email
    query = db.engine.execute(f"SELECT  *FROM `customer_vehicle` WHERE `customer_vehicle`.`email`='{em}'")
    return render_template('vehicle_info.html', query=query)

# Contact us Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Coming Soon Page
@app.route('/comingsoon')
def coming_soon():
    return render_template('coming_soon.html')

# Test Page
@app.route('/test')
def test():
    return render_template('test.html')


# To run the application
app.run(debug=True)
