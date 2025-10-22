from flask import Blueprint, jsonify, render_template
from .data_source import data_source_instance

bp = Blueprint("routes", __name__)

@bp.get("/")
def index():
    return render_template("dashboard.html")

@bp.get("/api/sensordata")
def sensordata():
    return jsonify(data_source_instance.get_all_data())

@bp.post("/api/clearalerts")
def clear_alerts():
    data_source_instance.clear_alerts()
    return jsonify({"status": "alerts cleared"})