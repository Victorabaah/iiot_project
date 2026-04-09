from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "v1")
APP_ENV = os.getenv("APP_ENV", "development")
DEVICE_GROUP = os.getenv("DEVICE_GROUP", "default-group")
MQTT_BROKER_URL = os.getenv("MQTT_BROKER_URL", "tcp://localhost:1883")
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "factory/default/telemetry")
HOSTNAME = socket.gethostname()


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "app": "edge-app",
        "version": APP_VERSION,
        "environment": APP_ENV,
        "deviceGroup": DEVICE_GROUP,
        "mqttBrokerUrl": MQTT_BROKER_URL,
        "mqttTopic": MQTT_TOPIC,
        "hostname": HOSTNAME,
        "status": "running"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/ready", methods=["GET"])
def ready():
    return jsonify({
        "status": "ready"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)