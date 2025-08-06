from flask import Flask, request, jsonify, redirect
import uuid

app = Flask(__name__)

# ========================
# In‑memory simulation data
# ========================
USERS = {
    "thanushamanjunath2233@gmail.com": {
        "id": "voicesight-user",
        "access_token": str(uuid.uuid4()),
        "refresh_token": str(uuid.uuid4())
    }
}

# Track dynamic device state so Google can test online/offline
DEVICE_STATE = {
    "camera-1": {
        "online": True,
        "on": True   # we expose OnOff so Google can flip state
    }
}

# ---------------- Root ----------------
@app.route("/")
def home():
    return "✅ VoiceSight Flask server is running!"

# ---------------- OAuth ---------------
@app.route("/oauth")
def oauth():
    redirect_uri = request.args.get("redirect_uri")
    state = request.args.get("state")
    auth_code = "sample-auth-code"
    return redirect(f"{redirect_uri}?code={auth_code}&state={state}")

# -------------- Token -----------------
@app.route("/token", methods=["POST"])
def token():
    grant_type = request.form.get("grant_type")
    email = "thanushamanjunath2233@gmail.com"

    if grant_type == "authorization_code":
        # generate fresh tokens
        USERS[email]["access_token"] = str(uuid.uuid4())
        USERS[email]["refresh_token"] = USERS[email]["refresh_token"]  # keep same for simplicity
        return jsonify({
            "token_type": "Bearer",
            "access_token": USERS[email]["access_token"],
            "refresh_token": USERS[email]["refresh_token"],
            "expires_in": 3600
        })

    elif grant_type == "refresh_token":
        refresh_token = request.form.get("refresh_token")
        if refresh_token != USERS[email]["refresh_token"]:
            return jsonify({"error": "invalid_grant"}), 400
        USERS[email]["access_token"] = str(uuid.uuid4())
        return jsonify({
            "token_type": "Bearer",
            "access_token": USERS[email]["access_token"],
            "expires_in": 3600
        })

    return jsonify({"error": "unsupported_grant_type"}), 400

# ------------- Smart‑Home -------------
@app.route("/smarthome", methods=["POST"])
def smarthome():
    body = request.get_json()
    intent = body["inputs"][0]["intent"]

    if intent == "action.devices.SYNC":
        return jsonify({
            "requestId": body["requestId"],
            "payload": {
                "agentUserId": "voicesight-user",
                "devices": [{
                    "id": "camera-1",
                    "type": "action.devices.types.CAMERA",
                    "traits": [
                        "action.devices.traits.CameraStream",
                        "action.devices.traits.OnOff"  # allow Google to toggle on/off (online)
                    ],
                    "name": {
                        "defaultNames": ["VoiceSight Camera"],
                        "name": "Smart Camera",
                        "nicknames": ["Front Door Cam"]
                    },
                    "willReportState": False,
                    "attributes": {
                        "cameraStreamSupportedProtocols": ["hls"],
                        "cameraStreamNeedAuthToken": False,
                        "cameraStreamNeedDrmEncryption": False
                    },
                    "deviceInfo": {
                        "manufacturer": "VoiceSight",
                        "model": "v1",
                        "hwVersion": "1.0",
                        "swVersion": "1.0"
                    }
                }]
            }
        })

    if intent == "action.devices.QUERY":
        return jsonify({
            "requestId": body["requestId"],
            "payload": {
                "devices": {
                    "camera-1": {
                        "on": DEVICE_STATE["camera-1"]["on"],
                        "online": DEVICE_STATE["camera-1"]["online"]
                    }
                }
            }
        })

    if intent == "action.devices.EXECUTE":
        cmds = body["inputs"][0]["payload"]["commands"]
        for cmd in cmds:
            for dev_id in cmd["ids"]:
                for execu in cmd["execution"]:
                    if execu["command"] == "action.devices.commands.OnOff":
                        DEVICE_STATE[dev_id]["on"] = execu["params"]["on"]
                        DEVICE_STATE[dev_id]["online"] = execu["params"]["on"]
        return jsonify({
            "requestId": body["requestId"],
            "payload": {
                "commands": [{
                    "ids": ["camera-1"],
                    "status": "SUCCESS",
                    "states": DEVICE_STATE["camera-1"]
                }]
            }
        })

    return jsonify({}), 400

# ----------- RequestSync stub ---------
@app.route("/requestsync", methods=["POST"])
def requestsync():
    # In real integration call Google HomeGraph API here
    print("[INFO] Simulated RequestSync call received.")
    return jsonify({"status": "OK"})

# -------------- Run server ------------
if __name__ == "__main__":
    app.run(port=8080, debug=True)
