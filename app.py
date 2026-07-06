import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from flask import make_response
import json

from ml.preprocessing import preprocess_data
from ml.clustering import run_clustering
from ml.interpretation import interpret_clusters

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def upload_page():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    k = int(request.form.get("clusters", 3))

    filename = secure_filename(file.filename)
    path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(path)

    df = pd.read_csv(path) if filename.endswith(".csv") else pd.read_excel(path)

    processed_df = preprocess_data(df)
    df["cluster"] = run_clustering(processed_df, k)

    results = interpret_clusters(df)

    return render_template("results.html", summary=results["summary"])


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/export")
def export():
    data = request.args.get("data")

    response = make_response(data)
    response.headers["Content-Type"] = "text/plain"
    response.headers["Content-Disposition"] = "attachment; filename=hris_report.txt"

    return response

if __name__ == "__main__":
    app.run(debug=True)