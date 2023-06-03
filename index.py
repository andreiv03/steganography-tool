from flask import Flask, render_template, request, redirect, send_file, jsonify
import os

from utils.encode import encode_image
from utils.decode import decode_image

server = Flask(__name__)


@server.route("/")
def index():
    return render_template("home.html")


@server.route("/image/encode", methods=["GET", "POST"])
def encode():
    if request.method == "POST":
        file = request.files["file"]
        message = request.form["message"]
        if not file or not message:
            return render_template("encode.html")

        encode_image(file, message)
        return redirect("/image/last/encoded")

    return render_template("encode.html")


@server.route("/image/last/encoded")
def last_encoded():
    last_encoded_image_path = os.path.join("static", "images", "encoded.png")

    if not os.path.exists(last_encoded_image_path):
        return redirect("/image/encode")

    return send_file(
        last_encoded_image_path, as_attachment=False, mimetype="image/png"
    )


@server.route("/image/decode", methods=["GET", "POST"])
def decode():
    if request.method == "POST":
        file = request.files["file"]
        if not file:
            return render_template("decode.html")

        decoded_message = decode_image(file)
        return jsonify({"message": decoded_message})

    return render_template("decode.html")


@server.route("/image/last/decoded")
def last_decoded():
    last_decoded_image_path = os.path.join("static", "images", "decoded.png")

    if not os.path.exists(last_decoded_image_path):
        return redirect("/image/decode")

    return send_file(
        last_decoded_image_path, as_attachment=False, mimetype="image/png"
    )


if __name__ == "__main__":
    server.run(debug=True)
