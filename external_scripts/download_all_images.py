"""this is a normal python that can be called from any location. It is not websepecific.

For the stable diffusion to read it as a new mode."""


import requests
import os

# Get the data from the endpoint
# this url need to be replaced by actual website url later.
response = requests.get('http://127.0.0.1:8000/api/images/')

# Make sure the request was successful
response.raise_for_status()

# Get the JSON data from the response
image_data = response.json()

# make sure output folder exists
output_folder = os.path.join(os.path.expanduser('~'), 'Desktop', "DB_images_preview")
os.makedirs(output_folder, exist_ok=True)

# delete all the files in this output folder
for filename in os.listdir(output_folder):
    os.remove(os.path.join(output_folder, filename))

# Iterate over the image data and download each image
for image in image_data:
    # Send a GET request to the image URL
    response = requests.get(image['url'])
    response.raise_for_status()
    
    # Create the path for the image file
    filename = os.path.join(output_folder, "DB_" + image['name'])
    
    # Write the image data to a file
    with open(filename, 'wb') as f:
        f.write(response.content)
        print (filename)

os.startfile(output_folder)
