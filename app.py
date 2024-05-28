from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_image_file():
   if request.method == 'POST':
      img = request.files['image']
      img_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(img.filename))
      img.save(img_path)
      description = request.form['description']
      # Save description to a text file
      with open(img_path + '.txt', 'w') as f:
         f.write(description)
      return 'Image and description saved.'

@app.route('/display/<filename>')
def display_image(filename):
   # Load the image
   img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
   img = cv2.imread(img_path)
   # Load YOLO
   net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
   layer_names = net.getLayerNames()
   output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
   # Detect cars
   blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
   net.setInput(blob)
   outs = net.forward(output_layers)
   # Draw bounding boxes
   for out in outs:
      for detection in out:
         scores = detection[5:]
         class_id = np.argmax(scores)
         if class_id == 2:  # Assuming that 'car' is class 2
            # Draw bounding box
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            cv2.rectangle(img, (center_x, center_y), (w, h), (0, 255, 0), 2)
   # Save the image
   cv2.imwrite(img_path, img)
   # Load the description
   description_path = img_path + '.txt'
   with open(description_path, 'r') as f:
      description = f.read()
   return render_template('display.html', filename=filename)

if __name__ == '__main__':
   app.run(debug = True)