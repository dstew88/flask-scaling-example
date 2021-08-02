from flask import Flask, send_from_directory

from .api.routes import bp as api_bp

app = Flask(__name__, static_url_path="")
app.register_blueprint(api_bp, url_prefix="/api")


@app.route("/")
def index():
    return send_from_directory("public", "index.html")
