import json, os, face_recognition
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from shutil import copyfile
from json import dumps

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
    dirpath = os.getcwd()
    database = dirpath + "/images/database"
    return compare_images(image.get("path"), database)

def compare_images(loaded_image_path, database):
    matched_images = []
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
            matched_images.append(image_path)

    print(matched_images)
    if matched_images:
        return make_response(dumps(matched_images))
    else:
        return jsonify(None)

# @app.route('/images', methods=['GET'])
# def get_files():
#     list_images = []
#     dirpath = os.getcwd()
#     database = dirpath + "/images/database"    
#     for image_file in os.listdir(database):
#         input_path = os.path.join(database, image_file)
#         image_obj = {
#             "name": image_file,
#             "path": input_path
#         }
#         list_images.append(image_obj)
#     return json.dumps(list_images)

@app.route('/save-image', methods=['POST'])
def save_file():
    image = request.get_json(force=True)
    back_path = os.getcwd() + "/images/database/" + image.get("name") + ".jpeg"
    front_path = os.path.dirname(os.getcwd()) + "/frontend/src/assets/images/database/" + image.get("name") + ".jpeg"
    copyfile(image.get("path"), back_path)
    copyfile(image.get("path"), front_path)
    return jsonify(image)

if __name__ == '__main__':
    app.run()


    
