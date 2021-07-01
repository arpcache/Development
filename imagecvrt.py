import sys
import os
from PIL import Image



# grab first and second Arg

#  Check if new / if not create


#loop through pokedex

a_directory = "./pokedex"

for filename in os.listdir(a_directory):
    #print(filename)
    img = Image.open(filename)
    img.save
    #print(img)
    #print(a_directory)




#convert to PNG