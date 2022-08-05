from flask import Flask, request, json, jsonify
import pandas as pd
import numpy as np
from PIL import Image
import preprocess
app = Flask(__name__)


@app.route('/SubmitFile', methods=["POST"])
def index():
    file = request.files['image']
    img = Image.open(file.stream)
    fen = preprocess.display_with_predicted_fen(image=file)
    print(fen)
        
    return jsonify({'msg': fen, 'size': [img.width, img.height]})





if __name__ == "__main__":
    app.run(debug=True)