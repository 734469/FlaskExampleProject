import cgi, os
import os.path as op
from typing import Optional
from typing import Union, Type
import requests
import json
from flask_admin import Admin, form
from flask import session as login_session
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from flask import Flask, render_template, url_for, redirect, request
from sqlalchemy.ext.hybrid import hybrid_property


UPLOAD_FOLDER = 'static'
admin = Admin()
app = Flask (__name__, static_folder='static')
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\734469\\Databases\\WeatherTwo.db'
app.config['SECRET_KEY'] = 'disum3rh9g'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Add air quality section for users to see and get advice on the air quality, provide default advice, get a place for extra user info (in another table maybe)
#user info table: User ID, City, avatar, medical conditions

db = SQLAlchemy(app)
admin.init_app(app)
file_path = op.join(op.dirname(__file__), 'static')
try:
    os.mkdir(file_path)
except OSError:
    pass

API = "8c843141480548dea9585310242302"
aqi = "yes"
#weather_url = f"http://api.weatherapi.com/v1/current.json?key={API}&q={city_name}&aqi={aqi}"

class Role(db.Model):
    __tablename__="role"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80))
    users = db.relationship("User", back_populates="role", lazy="dynamic")

    def __repr__(self):
        return f' {self.name}'


#Creating user
class User(db.Model, UserMixin):
    __tablename__ ="user"
    id = db.Column(db.Integer, primary_key=True) #primary key
    username=db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash: str = db.Column(db.String(100), nullable=False)
    role_code = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship("Role", back_populates="users")

    @hybrid_property
    def password(self) -> Union[str,None]:
        return self.password_hash

    @password.setter
    def password(self, password: str) -> None:
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

#def __ror__(self, other):


    def __repr__(self):
        return f'<User (self.username)>'


#loads user as something
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#user admin modelview
class UserView(ModelView):
    can_delete = False
    form_columns = ["username", "email", "password", "role"]
    column_list = ["username", "email", "password", "role"]


class RoleView(ModelView):
    form_columns = ["name"]
    column_list = ["name"]


admin.add_view(RoleView(Role, db.session))
admin.add_view(UserView(User, db.session))


@app.route('/')
@app.route('/home')
def homepage():
    #print(current_user.is_authenticated)
    return render_template('homepage.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        role_code = 2
        new_user = User(username=username, email=email, password_hash=hashed_password, role_code=role_code) #adds them as the account details to the admin setup
        db.session.add(new_user) #adds it to the database
        db.session.commit() #commits it do the database
        return redirect(url_for('login')) #moves user straight to login
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password_hash, password):
            login_session["username"] = username
            login_user(user)
            return redirect(url_for("homepage"))
        else:
            if "username" in login_session:
                return redirect(url_for("homepage"))
    return render_template("login.html")


@app.route('/dashboard')
def dashboard():
    city_name = "london"
    url = f"http://api.weatherapi.com/v1/current.json?key={API}&q={city_name}&aqi={aqi}"
    result = requests.get(url)
    weather_data = json.loads(result.text)
    weather_type = weather_data["current"]["condition"]["text"]
    city_name = weather_data["location"]["name"]
    return render_template('dashboard.html', weather_type=weather_type, city=city_name)


@app.route('/defaultWeather')
def homeframe1():
    weather_url = f"http://api.weatherapi.com/v1/current.json?key={API}&q=London&aqi={aqi}"
    london = requests.get(weather_url)
    #print(london)
    weather_data = json.loads(london.text)
    weather_lon = weather_data["current"]["condition"]["text"]
    country = weather_data["location"]["country"]
    wind = weather_data["current"]["wind_mph"]
    pressure = weather_data["current"]["pressure_mb"]
    rain = weather_data["current"]["precip_mm"]
    humidity =weather_data["current"]["humidity"]

    return render_template('defaultWeather.html', loc=weather_lon, country=country, wind=wind, pre=pressure, rain=rain, hum=humidity)


@app.route('/defaultWeather2')
def homeframe2():

    weather_url = f"http://api.weatherapi.com/v1/current.json?key={API}&q=NY&aqi={aqi}"
    nYork = requests.get(weather_url)
    weather_data = json.loads(nYork.text)
    weather_ny = weather_data["current"]["condition"]["text"]
    country = weather_data["location"]["country"]
    wind = weather_data["current"]["wind_mph"]
    pressure = weather_data["current"]["pressure_mb"]
    rain = weather_data["current"]["precip_mm"]
    humidity =weather_data["current"]["humidity"]

    return render_template('defaultWeather2.html', loc=weather_ny, country=country, wind=wind, pre=pressure, rain=rain, hum=humidity)


@app.route('/defaultWeather3')
def homeframe3():
    weather_url = f"http://api.weatherapi.com/v1/current.json?key={API}&q=Beijing&aqi={aqi}"
    beijing = requests.get(weather_url)
    weather_data = json.loads(beijing.text)
    #print(weather_data)
    weather_bei = weather_data["current"]["condition"]["text"]
    country = weather_data["location"]["country"]
    wind = weather_data["current"]["wind_mph"]
    pressure = weather_data["current"]["pressure_mb"]
    rain = weather_data["current"]["precip_mm"]
    humidity =weather_data["current"]["humidity"]

    return render_template('defaultWeather3.html', loc=weather_bei, country=country, wind=wind, pre=pressure, rain=rain, hum=humidity)

'''
@app.route('/weather-search', methods=['GET', 'POST'])
def weather_search():
    if request.method == "POST":
        city_name = request.form.get("city_name")

        weather_url = f"http://api.weatherapi.com/v1/current.json?key={API}&q={city_name}&aqi={aqi}"
        result = requests.get(weather_url)
        weather_data = json.loads(result.text)

        city_name = weather_data["location"]["name"]
        temp = weather_data["current"]["temp_c"]
    return render_template('weathersearch.html', city_name=city_name, temp=temp)
'''

@app.route('/weather-search', methods=['GET', 'POST'])
def weather_search():
    city_name = ""
    region = ""
    country = ""
    wind =""
    pressure =""
    rain =""
    humidity =""
    weather_cat = ""
    temp = ""
    time = ""
    if request.method == 'POST':
        city_name = request.form.get('city_name')
        url = f"http://api.weatherapi.com/v1/current.json?key={API}&q={city_name}&aqi={aqi}"
        result = requests.get(url)  # Will call the website and fetch information
        # successful response code is 200
        # data is more readable with json module
        weather_data = json.loads(result.text)

        city_name = weather_data["location"]["name"]

        region = weather_data["location"]["region"]
        country = weather_data["location"]["country"]
        time = weather_data["location"]["localtime"]
        weather_cat = weather_data["current"]["condition"]["text"]
        wind = weather_data["current"]["wind_mph"]
        temp = weather_data["current"]["temp_c"]
        pressure = weather_data["current"]["pressure_mb"]
        rain = weather_data["current"]["precip_mm"]
        humidity = weather_data["current"]["humidity"]
    return render_template("weathersearch.html", city_name=city_name, region = region, country=country, wind=wind, pre=pressure, rain=rain, hum=humidity, weather=weather_cat, temp=temp, time=time)


@app.route('/info')
def info():
    return render_template("info.html")

@app.route('/user-info')
def user_info():
    return render_template("user_info.html")


@app.route('/logout')
def logout():
    del login_session['username']
    logout_user()
    return redirect(url_for('homepage'))


@app.route('/Ts&Cs')
def term_conds():
    return render_template("terms.html")


@app.route('/graph')
def graph():
    labels = ["Thing 1", "Thing 2", "Thing 3"]
    data = [23, 47, 29]
    return render_template("graph.html", data=data, labels=labels)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)