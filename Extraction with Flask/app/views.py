from app import app
from flask import request, render_template, url_for
import os
import cv2
import numpy as np
from PIL import Image
import random
import string
import pytesseract

# adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'

#Route to home page
@app.route("/", methods = ['GET', 'POST'])

def index():

    # Execute if request is get
    if request.method == "GET":
        full_filename = 'images/white_bg.jpg'
        return render_template("index.html", full_filename = full_filename)
    
    # Execute if request is post
    if request.method == "POST":
        image_upload = request.files['image_upload']
        image = Image.open(image_upload)

        # COnverting image to rgb
        image_arr = np.array(image.convert('RGB'))
        # Converting image to grayscale
        gray_img_arr = cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)
        # Converting image back to array
        image = Image.fromarray(gray_img_arr)

        # printing lowercase
        letters = string.ascii_lowercase
        # Generating unique image name for dynamic image display
        name = ''.join(random.choice(letters) for i in range(10)) + '.jpg'
        full_filename = 'uploads/'+ name

        # Extracting text from image
        text = pytesseract.image_to_string(image, lang='eng')

        #Remove symbol if any
        characters_to_remove = "!—*“>+-/|£#%$^_~"
        new_string = text
        for character in characters_to_remove:
            new_string = new_string.replace(character, "")

        # Converting string into list to display extcated text in seperate line
        new_string = new_string.split("\n")

        # Saving image to display in html
        img = Image.fromarray(image_arr, 'RGB')
        img.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], name))
        # Returning template, filename, extracted text
        return render_template('index.html', full_filename = full_filename, text = new_string)
    
# Main function
if __name__ == '__main__':
    app.run(debug=True)