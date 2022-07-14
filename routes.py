from flask import Flask, jsonify, request
import pixels

app = Flask(__name__)

@app.route("/")
def home():
    res = {
        "author": "Ayush Kumar",
        "usage": "use POST /image-pixels formatted as {'dimensions': [rows, columns], 'corner_points': [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] }"
    }
    return jsonify(res)


@app.route('/image-pixels', methods=['POST'])
def image_pixels():
    data = request.get_json()
    if pixels.is_input_valid(data):
        m, n = data['dimensions']
        corner_points = data['corner_points']
        solution = pixels.generate_pixels(m, n, corner_points)
        return jsonify({'solution': solution})
    else:
        return jsonify({'status' : 'Invalid data'})