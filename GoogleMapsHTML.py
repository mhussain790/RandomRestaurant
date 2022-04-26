# Annie Wan
# CS 361
# Microservice for Masud Hussain
# Generating an HTML iframe element for the Google Maps location of a given address

from time import sleep


# Check the status.txt file to see if an iframe needs to be generated
def check_run_status():
    while True:
        with open('status.txt', 'r') as check:
            status = check.readline()
            if status == 'run':
                check.close()
                create_iframe()
                check = open('status.txt', 'r+')
                check.truncate()
            sleep(1)    # Change this to however often you'd like status.txt to be checked


# Retrieve the address from the address.txt file,
# create the iframe, and write it to the address.txt file
def create_iframe():
    random_restaurant = open("address.txt", "r+")
    restaurant_address = random_restaurant.read()
    restaurant_address = restaurant_address.replace(" ", "%20")

    # Put together the embed URL
    embed_start = "https://maps.google.com/maps?q="
    embed_end = "&t=&z=17&ie=UTF8&iwloc=&output=embed"
    embed_src = embed_start + restaurant_address + embed_end

    # Put together the HTML iframe element
    # iframe_start = "<iframe id=\"google_maps_embed\" width=\"400\" height=\"400\" src=\""
    # iframe_end = "\"></iframe>"
    # complete_iframe = iframe_start + embed_src + iframe_end
    # print(complete_iframe)

    # Write the HTML iframe element to the shared text file
    random_restaurant.seek(0)
    random_restaurant.truncate()      # Overwrite the entire file contents
    random_restaurant.write(embed_src)
    random_restaurant.close()


if __name__ == "__main__":
    check_run_status()
