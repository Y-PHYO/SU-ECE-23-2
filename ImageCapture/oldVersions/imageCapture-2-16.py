# Import opencv for computer vision
import cv2
import time

# Import matplotlib so we can visualize an image
from matplotlib import pyplot as plt

from PIL import Image, ImageChops

# Let's image title be change easily
imageTitle = "Calibrate-Images"

# Let's number of images to be taken be changed easily
numIms = 5

# Select a camera
# USB connected -- 0 = USB Cam -- 1 = laptop -- 2 = phone
# USB NOT connected -- 0 = laptop -- 1 = phone

camera = 0


# Takes photo and stores it with title chosen above
def takePhoto(counter, title):
    val = str(counter)

    cap = cv2.VideoCapture(camera) # when usb connected 0 = usbcam, 1 = laptop, 2 = phone            when usb NOT connected 0 = laptop, 1 = phone
    # Get frame from device
    ret, frame = cap.read()

    # Provides preview image to the right as a plot
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.show()

    # Writes the photo to a file
    cv2.imwrite("imagesFolder/" + title + "-" + val + ".JPEG", frame)
    # Releases webcam to be used elsewhere
    cap.release()

    counter += 1

    return counter


# Runs loop of num of photos
def capPhoto():
    for i in range(0, numIms):
        takePhoto(i, imageTitle)
        print(i)
        time.sleep(5)


# Finds difference between two photos in this folder
# Assumes user can input path to photo as string when using the function
# https://www.geeksforgeeks.org/spot-the-difference-between-two-images-using-python/
def findDifference(image1, image2):
    img1 = Image.open(image1)
    img2 = Image.open(image2)

    diff = ImageChops.difference(img1, img2)

    diff.save("imagesFolder/" + imageTitle + "-" + "difference" + ".JPEG", "JPEG")

    diff.show()


