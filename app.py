from flask import Flask, render_template, json, redirect, url_for
from flask.helpers import flash
from flask_mysqldb import MySQL
from flask import request
from flask_bootstrap import Bootstrap
import random
import time
import json
import requests
import os

# Configuration

app = Flask(__name__, template_folder='templates')
Bootstrap(app)

client_id = "1BuLr6ex0bHofbTEM_YtnA"
yelp_key = "EehGoSyE1VtckLyECKp82rzTJWM1QL5qpiSAb6SeEP2DRDghOOEEL1z6mC9-1uhIw65rUzK7AHsPPw0c91R4mi1ea_er9PnBYzU0neoC-QhOOHPSnvaMLDRVC68WYnYx"


# ROOT method
# Renders the index.html page and generates the random restaurants using API call and microservice.
# 

@app.route('/', methods=['GET', 'POST'])
def root():
    # Output data to template
    output_data = []
    iframe = ''

    # Store Yelp food categories in json_data
    json_data = getCategories()

    if request.method == 'POST':

        # Stored user input data from form
        user_zip_code = request.form['zip']
        user_food_type = request.form['food-type']
        user_distance = request.form['distance']

        # update variables with user entered data
        location = "location=" + user_zip_code
        categories_info = "categories=" + user_food_type + "&"
        distance = "distance=" + user_distance + "&"

        URL = "https://api.yelp.com/v3/businesses/search?"

        # Build API call
        query = URL + categories_info + distance + location
        headers = {'Authorization': 'Bearer %s' % yelp_key}
        params = {'term': 'seafood', 'location': 'new york city'}
        req = requests. get(query, headers=headers)

        print('Status code is {}' .format(req.status_code))
        
        items = req.json()
        business = items['businesses']

        # Generate Random Num and Random Restaurant
        random_num = random.randrange(0, len(business))
        
        street_name = items['businesses'][random_num]['location']['address1']
        city = items['businesses'][random_num]['location']['city']
        state = items['businesses'][random_num]['location']['state']
        zip_code = items['businesses'][random_num]['location']['zip_code']
        address = street_name + " " + city + " " + state + " " + zip_code

        # Store restaurant info in vars to output data
        restaurant_name = items['businesses'][random_num]['name']
        restaurant_rating = items['businesses'][random_num]['rating']
        restaurant_price = items['businesses'][random_num]['price']

        # Write address to address.txt file
        with open('address.txt', 'w+') as g:
            g.write(address)
        
        # Open status.txt and write run
        with open('status.txt', 'w+') as h:
            h.write('run')
        
        # Sleep for 2 seconds
        time.sleep(2)

        # Clear status.txt
        with open('status.txt', 'w+') as j:
            j.truncate()

        time.sleep(3)

        with open('address.txt', 'r+') as k:
            iframe = str(k.read())

        # Add restaurant info and iframe to output_data
        output_data.append(iframe)
        output_data.append(restaurant_name)
        output_data.append(restaurant_rating)
        output_data.append(restaurant_price)

        return render_template('index.html', category_data=json_data, output_data=output_data)

    return render_template('index.html', category_data=json_data, output_data=output_data)


def getCategories():
    with open('categories.json') as f:
        json_data = json.load(f)

    return json_data

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9113))
    #                                 ^^^^
    #              You can replace this number with any valid port

    app.run(port=port, debug=True)
