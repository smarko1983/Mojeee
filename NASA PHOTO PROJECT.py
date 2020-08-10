# NASA Photo Project

# Information that we already have

# Information 1: Curiosity takes images at 1600x1200 pixels, with 8 bits per pixel.
# Information 2: Curiosity can transmit data at:
# 1. 2000kbit/s to the Mars Reconnaissance Orbiter for 8 mins per day;
# 2. 256kbit/s to the Odyssey Orbiter for 8 mins per day;
# 3. 32kbit/s directly to Earth.
# Information 3: number of images used to combine into one big image - exactly 1000


# The program itself...

side1 = int(input("How many pixels are on the first side: "))
side2 = int(input("How many pixels are on the second side: "))
bit_depth = int(input("What is the bit depth of the image:  "))
num_of_images = int(input("Please enter the number of images: "))

image_size = (side1 * side2 * bit_depth) / 1000   # per one image, in kbits
print("The image size of one image is: ", image_size, " kilobits")          # per one image, in kbits
# I am going to express the image size in kbits.  I divided by 1000 to convert it to from bits to  kilobits.
# [Btw, if you are wondering why I converted it by 1000,
# and not by 1024, belive me that the answer to that question is complicated :) and you could do that, and some people would say that I
# am correct for doing that while the others would disagree. Anyways, I am going to post a few interesting videos and links on that topic,
# you can view this as an introduction to it :) ]

thousand_images = 1000 * image_size
print("The size of one thousand images is ", thousand_images, " kbits/s")
# Now we got our 1000 images (expressed in kbit) that we can see how are we going to transfer to earth

Reconnaissance = 60 * 2000 * 8  # because 2000kbits/s, I am multiplying that per 60s to get one minute, and then multiplying by 8 to see how many kbits
# can it transfer per 8 minutes
Odyssey = 60 * 256 * 8  # the same as above
Earth_directly = 60 * 32 * (24 * 60 - 8 - 8)  # now, since we don't need Reconnaissance and Odyssey time, we subtract that from the total number of minutes
print("Reconnaissance transmits ", Reconnaissance, " kbits per day, Odyssey transmits  ", Odyssey, \
      " kbits per day, and ",  Earth_directly, " kbits goes to earth directly")

kbits_per_day = Reconnaissance + Odyssey + Earth_directly
print("Per one day, I can send  ", kbits_per_day, " kbits")


days_to_transmit = thousand_images / kbits_per_day
print(days_to_transmit)
print("it would take us at least ", int(days_to_transmit), " days to transmit an image from Mars to Earth")
# I used int( ) function to remove the decimal part of the number





