from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
import json, cv2, os, face_recognition


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/recognition', methods=['POST'])
def recognition():
    image = request.get_json(force=True) 
    database = "/Users/fabiomarques/Downloads/python/project_flask/server/images/database"
    return compare_images(image.get("path"), database)

def compare_images(loaded_image_path, database):
    for image_path in os.listdir(database):
        input_path = os.path.join(database, image_path)

        face_to_rec = face_recognition.load_image_file(input_path)
        face_to_rec_encode = face_recognition.face_encodings(face_to_rec)[0]

        loaded_image = face_recognition.load_image_file(loaded_image_path)
        loaded_image_encode = face_recognition.face_encodings(loaded_image)[0]

        known_face_encodings = [face_to_rec_encode]
        loaded_face_encodings = [loaded_image_encode]

        for face in loaded_face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face)

        if True in matches:
            return jsonify(os.path.join(database, image_path))
        else:
            return jsonify(False)

@app.route('/images', methods=['GET'])
def get_files():
    database = "/Users/fabiomarques/Downloads/python/project_flask/server/images/database"
    list_images = []
    print(os.listdir(database))
    for image_path in os.listdir(database):
        print(image_path)
        list_images.append(image_path)
    return jsonify(json.dumps(list_images))


if __name__ == '__main__':
    app.run()


    
