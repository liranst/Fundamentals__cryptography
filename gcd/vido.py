import cv2
import os

images_path = r'C:\Users\97252\Fundamentals__cryptography\gcd'

image_files = [img for img in os.listdir(images_path) if img.endswith(".png")]
image_files.sort(reverse=False)
print(image_files)
# Get the first image to extract its dimensions
first_image = cv2.imread(os.path.join(images_path, image_files[0]))
height, width, layers = first_image.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('x.avi', fourcc, 1.4, (width, height))

# Loop through all images and add them to the video
for image_file in image_files:
    image_path = os.path.join(images_path, image_file)
    frame = cv2.imread(image_path)
    video.write(frame)

# Release the video writer
video.release()

print("Video created successfully!")
