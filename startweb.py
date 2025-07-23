#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request, url_for
from flask_autoindex import AutoIndex

# Create a Flask application instance
app = Flask(__name__, static_folder="public/static", template_folder="public")
# Create an AutoIndex instance for serving directory listings
auto_index = AutoIndex(app, browse_root="./public/user", add_url_rules=False)


# Define a route for the root URL ("/")
@app.route("/")
def index():
    return render_template("index.html")


# Define a route for handling file uploads via POST request to "/upload_action"
@app.route("/upload_action", methods=["POST"])
def upload_action():
    url = request.host_url
    file = request.files["upfile"]

    # Check if a file was selected for uploading
    if not file:
        return f"""
            <div style="
                font-size: 1.8rem;
                text-align: center;
                align-items: center;
            ">
            <p style="margin-bottom: 0.5em;">No file selected for uploading.</p>
            <button
                onclick="window.close()" 
                style="
                    padding: 0.8em;
                    background-color: gray;
                    color: white;
                    text-decoration: none;
                    border: none;
                    border-radius: 0.4em;
                    font-size: 1.8rem;
                    cursor: pointer;
                "
            >Close</button>
            </div>
            """
    
    strFilename = file.filename  # secure_filename(file.filename) or urllib.parse.quote(file.filename)
    # file.filenameに()が含まれていたら（）に置換する
    strFilename = strFilename.replace("(", "（").replace(")", "）")

    strPath = os.path.join("public", "user", strFilename)
    # print(strPath)
    file.save(strPath)
    # 戻るボタンとアップロード確認ボタンを表示するHTMLを返す
    return f"""
        <div style="
            font-size: 1.8rem;
            text-align: center;
            align-items: center;
        ">
        <p style="margin-bottom: 0.5em;">{strFilename}</p>
        <p style="margin-bottom: 0.5em; color: green;">Upload succeeded.</p>
        <button
            onclick="window.close()" 
            style="
                padding: 0.8em;
                background-color: gray;
                color: white;
                text-decoration: none;
                border: none;
                border-radius: 0.4em;
                font-size: 1.8rem;
                cursor: pointer;
            "
        >Close</button>
        </div>
        """


# Define a route for serving directory listings using AutoIndex
@app.route("/serve/")
@app.route("/serve/<path:path>")
def autoindex(path="."):
    return auto_index.render_autoindex(path)


# Run the Flask application if this script is executed directly
if __name__ == "__main__":
    LOCAL_MODE = os.path.exists(os.path.expanduser("./debug"))
    # Run the application in debug mode with the specified host and port
    if LOCAL_MODE:
        app.run(debug=True, host="127.0.0.1", port=80)
    else:
        app.run(debug=True, host="0.0.0.0", port=80)
