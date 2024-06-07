import tkinter as tk
from tkinter import ttk
from home import homePage
from help import helpPage
from question_input import inputPage
from question_display import displayPage
from feedback_correct import feedbackCorrectPage
from feedback_incorrect import feedbackIncorrectPage
from finish import finishPage

import threading
import subprocess
import time

# image handling imports
from MangDang.mini_pupper.display import Display, BehaviorState
from resizeimage import resizeimage  # library for image resizing
from PIL import Image, ImageDraw, ImageFont # library for image manip.
 
LARGEFONT =("Verdana", 35)
MEDIUMFONT =("Verdana", 25)

# Display settings
MAX_WIDTH = 320
# Get access to the display so we can display things
disp = Display()
        
# Two images path
image_eyes_closed = "images/eyes_closed.png"
image_eyes_opened = "images/eyes_opened.png"
        
# Initialize a list with image identifiers for different eyes
all_images = ['image_eyes_closed', 'image_eyes_opened']
# List of corresponding image file attributes for each identifier
all_images_pngfile = [image_eyes_closed, image_eyes_opened]
        
# Initialize an empty list to store resized image files
new_images = []


# Loop through each image identifier in the list
for img in all_images:
    # Open the image file corresponding to the current identifier and store it in an attribute
    imgFile = Image.open(all_images_pngfile[all_images.index(img)])
        
    # Convert to RGBA if needed
    if (imgFile.format == 'PNG'):
        if (imgFile.mode != 'RGBA'):
            imgOld = imgFile.convert("RGBA")
            imgFile = Image.new('RGBA', imgOld.size, (255, 255, 255))

    # We likely also need to resize to the pupper LCD display size (320x240).
    # Note, this is sometimes a little buggy, but you can get the idea. 
    width_size = (MAX_WIDTH / float(imgFile.size[0]))
    imgFile = resizeimage.resize_width(imgFile, MAX_WIDTH)

    newFileLoc = 'images/' + img + 'RZ.png'   #rename as you like
    new_images.append(newFileLoc)
            
    # now output it (super inefficient, but it is what it is)
    imgFile.save(newFileLoc, imgFile.format)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (homePage, helpPage, inputPage, displayPage, feedbackCorrectPage, feedbackIncorrectPage, finishPage):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(homePage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.configure(bg="#f9cb9c")
        #self.geometry("1024x600")

        # Every time input question page accessed, play input question audio
        if isinstance(frame, inputPage):
            frame.playAudioThread()
        # Every time question display page accessed, wait for sensor input
        if isinstance(frame, displayPage):
            frame.waitForSensorInputThread()
        # Every time correct page accessed, play barking audio
        if isinstance(frame, feedbackCorrectPage):
            frame.playAudioThread()
        # Every time incorrect page accessed, play growling audio
        if isinstance(frame, feedbackIncorrectPage):
            frame.playAudioThread()
        # Every time finish page accessed, play congratulatory audio
        if isinstance(frame, finishPage):
            frame.playAudioThread()


###
# Name: runBackgroundTask
# Purpose: Run a thread to give Tutorpup idle facial expressions
# @input  None
# @return None
#####    
def runBackgroundTask():
    # Keep running for the entire session
    while True:                   
        disp.show_image(new_images[1])	# Display the corresponding facial expression for eyes open
        time.sleep(3)	# Pupper's eyes open for 3 seconds
           
        # Pupper's eyes close for 1 seconds
        disp.show_image(new_images[0])    # Display the corresponding facial expression for eyes close
        time.sleep(0.5)	# Pupper's eyes close for 0.5 seconds

# Driver Code
if __name__ == "__main__":
    app = tkinterApp()
    #app.geometry("1024x600")
    app.title("TutorPup")

    # Background Task (for pupper idle expressions)
    backgroundTask = threading.Thread(target=runBackgroundTask, args=())
    print ("background task thread started")
    backgroundTask.daemon = True
    backgroundTask.start()

    app.mainloop()