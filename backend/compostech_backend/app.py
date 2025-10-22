import os
import threading
from flask import Flask
from .routes import bp
from . import mqtt_client

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.register_blueprint(bp)
    return app

app = create_app()

def _mqtt():
    mqtt_client.start_loop()

if __name__ == "__main__":
    t = threading.Thread(target=_mqtt, daemon=True)
    t.start()
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "5000"))
    app.run(host=host, port=port, debug=False)