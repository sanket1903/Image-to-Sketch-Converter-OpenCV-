import cv2
import matplotlib.pyplot as plt
import numpy as np

# Define the input image path
input_image_path = 'D:\\sketch\\file.png'

# Load the image from the specified file
img = cv2.imread(input_image_path)

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
img_invert = cv2.bitwise_not(img_gray)

# Smooth the sharp edges in the image while minimizing too much blurring
img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), 0)

# Invert the blurred image
inverted_blur = cv2.bitwise_not(img_smoothing)

# Create a sketch by dividing the grayscale image by the inverted blurred image
final = cv2.divide(img_gray, inverted_blur, scale=256.0)

# Darkening the final image
dark_factor = 0.4 # Adjust this value to control darkness (0.0 - 1.0)
darkened_final = np.clip(final * dark_factor, 0, 255).astype(np.uint8)

# Plotting the images
plt.figure(figsize=(20, 20))

plt.subplot(1, 5, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("Original Image")

plt.subplot(1, 5, 2)
plt.imshow(img_gray, cmap="gray")
plt.axis("off")
plt.title("GrayScale Image")

plt.subplot(1, 5, 3)
plt.imshow(img_invert, cmap="gray")
plt.axis("off")
plt.title("Inverted Image")

plt.subplot(1, 5, 4)
plt.imshow(img_smoothing, cmap="gray")
plt.axis("off")
plt.title("Smoothen Image")

plt.subplot(1, 5, 5)
plt.imshow(darkened_final, cmap="gray")
plt.axis("off")
plt.title("Darkened Final Sketch Image")

plt.show()

# Define the output image path
output_image_path = 'D:\\sketch\\final_sketch_dark.png'

# Save the darkened final sketch image to the specified output path
cv2.imwrite(output_image_path, darkened_final)
