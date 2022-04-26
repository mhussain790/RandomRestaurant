import requests
import json
import random

client_id = "1BuLr6ex0bHofbTEM_YtnA"
yelp_key = "EehGoSyE1VtckLyECKp82rzTJWM1QL5qpiSAb6SeEP2DRDghOOEEL1z6mC9-1uhIw65rUzK7AHsPPw0c91R4mi1ea_er9PnBYzU0neoC-QhOOHPSnvaMLDRVC68WYnYx"

# headers = {'Authorization': 'Bearer %s' % yelp_key}

# url = 'https://api.yelp.com/v3/businesses/search'

# params = {'term': 'seafood', 'location': 'new york city'}

# req = requests. get(url, params=params, headers=headers)

# print('Status code is {}' .format(req.status_code))
# # json.loads(req.text)

# with open('categories.json') as f:
#     json_data = json.load(f)

#     for i in json_data:
#         print(i)
URL = "https://api.yelp.com/v3/businesses/search?"
categories_info = "categories=steak&"
distance = "distance=5&"
location = "location=91001"

query = URL + categories_info + distance + location

headers = {'Authorization': 'Bearer %s' % yelp_key}

params = {'term': 'seafood', 'location': 'new york city'}

req = requests. get(query, headers=headers)

print('Status code is {}' .format(req.status_code))
# json.loads(req.text)
# print(req.text)
items = req.json()


business = items['businesses']

random_num = random.randrange(0, len(business))
print(random_num)
print(items['businesses'][random_num]['name'])
print(items['businesses'][random_num]['rating'])
print(items['businesses'][random_num]['price'])
print(items['businesses'][random_num]['location']['address1'])
print(items['businesses'][random_num]['location']['city'])
print(items['businesses'][random_num]['location']['state'])
print(items['businesses'][random_num]['location']['zip_code'])

def root(): 
    iframe = '' 
    
    with open('categories.json') as f: json_data = json.load(f) 
    
    if request.method == 'POST': 
        URL = "https://api.yelp.com/v3/businesses/search?" 
        
        # get user entries from form 
        user_category = request.form['category'] 
        user_distance = request.form['distance'] 
        user_zip = request.form['zip_code'] 

        categories_info = "categories=" + user_category +"&" 
        distance = "distance=" + user_distance + "&" 
        location = "location=" + user_zip 
        
        query = URL + categories_info + distance + location 
        
        headers = {'Authorization': 'Bearer %s' % yelp_key} 
        req = requests. get(query, headers=headers) 
        print('Status code is {}' .format(req.status_code)) 
        
        # convert req into dict 
        items = req.json() 
        business = items['businesses'] 
        
        # generate random number using generated restaurants as a range 
        random_num = random.randrange(0, len(business)) 
        
        # get address data for the restaurant 
        street_name = items['businesses'][random_num]['location']['address1'] 
        city = items['businesses'][random_num]['location']['city'] 
        state = items['businesses'][random_num]['location']['state'] 
        zip_code = items['businesses'][random_num]['location']['zip_code'] 
        
        address = street_name + " " + city + " " + state + " " + zip_code 
        
        # write address to address.txt so microservice can generate google maps iframe 
        with open('address.txt', 'w+') as g: g.write(address) 
        
        # write run to status.txt to run microservice 
        with open('status.txt', 'w+') as h: 
            h.write('run') 
        
        time.sleep(2) 
            
        # Clear status.txt 
        with open('status.txt', 'w+') as j: 
            j.truncate() 
        
        time.sleep(3) 
        
        # read address.txt file 
        with open('address.txt', 'r+') as k: 
            iframe = k.read() 
        
        return redirect((url_for('root', output_data=iframe))) 
    return render_template('index.html')