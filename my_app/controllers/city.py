from my_app import app
from flask import render_template, redirect, request, session
from my_app.models.cities import City

@app.route('/cities')
def cities():
	return render_template('index.html',cities=City.get_all())
        


