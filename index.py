from flask import Flask, abort, jsonify, redirect, render_template, request, send_file
import os

from utils.config import STATIC_IMAGES_DIR
from utils.decode import decode_image
from utils.encode import encode_image

server = Flask(__name__)


@server.route("/")
def index():
    return render_template("home.html", active_page="home")


@server.route("/image/encode", methods=["GET", "POST"])
def encode():
    if request.method == "POST":
        file = request.files.get("file")
        message = request.form.get("message")
        if not file or not message:
            return abort(400, description="File and message fields are required!")

        encode_image(file, message)
        return redirect("/image/last/encoded")

    return render_template("encode.html", active_page="encode")


@server.route("/image/last/encoded")
def last_encoded():
    encoded_image_path = os.path.join(STATIC_IMAGES_DIR, "encoded.png")

    if not os.path.exists(encoded_image_path):
        return abort(404, description="Encoded image not found!")

    return send_file(encoded_image_path, mimetype="image/png")


@server.route("/image/decode", methods=["GET", "POST"])
def decode():
    if request.method == "POST":
        file = request.files.get("file")
        if not file:
            return abort(400, description="File field is required!")

        decoded_message = decode_image(file)
        return jsonify({"message": decoded_message})

    return render_template("decode.html", active_page="decode")


@server.route("/image/last/decoded")
def last_decoded():
    decoded_image_path = os.path.join(STATIC_IMAGES_DIR, "decoded.png")

    if not os.path.exists(decoded_image_path):
        return abort(404, description="Decoded image not found!")

    return send_file(decoded_image_path, mimetype="image/png")


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)
