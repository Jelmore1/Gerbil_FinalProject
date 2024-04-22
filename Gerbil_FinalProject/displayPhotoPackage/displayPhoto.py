# Name: Jared Turner
# email: turne2jw@mail.uc.edu
# Assignment Number: Final Project
# Due Date:04/23/24
# Course/Section: IS4010-001
# Semester/Year: spring 2024
# Brief Description of the assignment:This project dcryptys files to find out where to go and what movie you have
# Brief Description of what this module does. This module loads and displays a photo
# Citations: 


from PIL import Image

import os



def loadPhoto(photo_path):

   """

   Loads and displays the photo from the specified path.

   @arg The path to the photo file.

   @return The loaded image.

   """

   image = Image.open(photo_path)

   image.show()

   return image



def displayPhoto():

   """

   Main function to load and display the photo.

   """

   photo_path = 'Group_Photo.jpg'  # Replace 'group_photo.jpg' with the actual path to your photo file

   loadPhoto(photo_path)