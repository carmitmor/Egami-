# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

#  # <img src="https://icons.iconarchive.com/icons/dtafalonso/android-l/72/Play-Games-icon.png"/>Egami Game: Opposite & color inverted picture
#
# ---

# ### <img src="https://img.icons8.com/bubbles/50/000000/information.png" style="height:50px;display:inline"> Student Information
# ---
#
#
#
#
# | #       |              Name |             Id |             email |
# |---------|-------------------|----------------|------------------ |
# |Student 1|  Ariel Lulinsky   |   315837138    | ariellu@campus.technion.ac.il
# |Student 2|  Carmit Mordechai |   315822577    | carmitmor@campus.technion.ac.il|

# +
# imports we need

import numpy as np
import matplotlib
mpl_data_dir = matplotlib.get_data_path()
from matplotlib import pyplot as plt
from skimage import transform

# -

def invert_image(image_name):
    """"
    :param image: The image to invert.
    :return: An inverted and rotated by 180 degree image.
    """
    image = plt.imread(image_name +".jpeg")
    rotational_image = transform.rotate(image, 180)
    rotational_image_new = np.array(rotational_image.copy())

    red = rotational_image[:,:,0]
    green = rotational_image[:,:,1]
    blue = rotational_image[:,:,2]

    red_new = np.array(red.copy())
    green_new = np.array(green.copy())
    blue_new = np.array(blue.copy())
    nrow,ncol = np.shape(red_new)
    for i in range(nrow):
        for j in range(ncol):
            red_new[i,j] = 1-red[i,j]
            green_new[i,j] = 1-green[i,j]
            blue_new[i,j] = 1-blue[i,j]

    colors = [red_new, green_new, blue_new]        

    for i in range(3):
        rotational_image_new[:,:,i] = colors[i]

    plt.imshow(rotational_image_new) 
    plt.title("\nopposite & inverted\n image of "+image_name, fontsize = 15), plt.xticks([]), plt.yticks([])
    plt.axis('off')    

    plt.show()
   


# +
image_name = input("Please enter the name of the image which is saved in your folder: " )

invert_image(image_name)
# -

#  # <img src="https://trump.org.il/wp-content/uploads/2016/06/720.b197b0.webp"/>
