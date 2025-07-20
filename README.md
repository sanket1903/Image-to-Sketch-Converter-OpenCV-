# Image-to-Sketch-Converter-OpenCV-

This Python project transforms any image into a pencil sketch using OpenCV techniques like grayscale conversion, inversion, Gaussian blurring, and image blending.

## ✨ Features
- Convert any image into a sketch-style drawing
- Adjustable darkening factor for custom intensity
- Side-by-side visualization of all transformation steps
- Final sketch image saved automatically

## 🖥️ Technologies Used
- Python
- OpenCV
- Matplotlib
- NumPy

## 📦 Installation
```bash
pip install opencv-python matplotlib numpy
🚀 How to Use
Place your input image in your local directory.

Update the input_image_path and output_image_path in sketch.py file:

python

input_image_path = 'D:\\sketch\\file.png'
output_image_path = 'D:\\sketch\\final_sketch_dark.png'
Run the script:

bash

python sketch.py
The sketch will be displayed and saved at the given path.
