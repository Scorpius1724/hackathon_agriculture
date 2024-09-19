from flask import Flask, render_template, request
import os
from filepath import find_filepath
from predict import prediction

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/upload", methods=["POST"])
def upload():
    if 'image' not in request.files:
        return "No file part", 400

    file = request.files['image']

    if file.filename == '':
        return "No selected file", 400

    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        latest_image_path = find_filepath(app.config['UPLOAD_FOLDER'])

        predict = prediction(latest_image_path)

        if latest_image_path:
            print(f"Latest image path: {latest_image_path}")
        else:
            print("No images found after upload.")

        return f"The prediction for your image is {predict}"

if __name__ == "__main__":
    app.run(debug=True)
