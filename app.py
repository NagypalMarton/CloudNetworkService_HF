from flask import Flask, request, jsonify, send_file
from flask_pymongo import PyMongo
import requests
import os

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/car_detection_db"
mongo = PyMongo(app)

UPLOAD_FOLDER = 'uploads'
DETECTED_FOLDER = 'detected'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DETECTED_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files or 'description' not in request.form:
        return jsonify({'error': 'No image or description provided'}), 400

    image = request.files['image']
    description = request.form['description']
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    # Call the car detection model (assuming a REST API call)
    detection_result = detect_cars(image_path)

    # Save to MongoDB
    image_entry = {
        'description': description,
        'image_path': image_path,
        'detections': detection_result['detections']
    }
    mongo.db.images.insert_one(image_entry)

    return jsonify({'message': 'Image uploaded and processed', 'detections': detection_result['detections']}), 201

def detect_cars(image_path):
    # Placeholder function for car detection
    # Replace with actual model call, e.g., requests.post('MODEL_URL', files={'image': open(image_path, 'rb')})
    return {'detections': [{'x': 100, 'y': 100, 'width': 50, 'height': 50}]}

@app.route('/images/<image_id>', methods=['GET'])
def get_image(image_id):
    image_entry = mongo.db.images.find_one({'_id': ObjectId(image_id)})
    if not image_entry:
        return jsonify({'error': 'Image not found'}), 404

    return send_file(image_entry['image_path'])

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    if not email:
        return jsonify({'error': 'No email provided'}), 400

    mongo.db.subscribers.insert_one({'email': email})

    # Send notifications for all existing images
    for image in mongo.db.images.find():
        send_notification(email, image)

    return jsonify({'message': 'Subscribed successfully'}), 201

def send_notification(email, image):
    # Placeholder function for sending email notifications
    # Replace with actual email sending logic
    pass

if __name__ == '__main__':
    app.run(debug=True)
