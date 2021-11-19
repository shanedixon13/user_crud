from flask import Flask, request
from datetime import datetime

app= Flask(__name__)

from app.database import user


@app.route("/")
def version():
    out={
        "ok": True,
        "message":"Success",
        "server_time":datetime.now().strftime("%F %H:%M:%S"),
        "version": "1.0.0"
    }
    return out

@app.route("/users", methods=["POST"])
def create_user():
    user_data = request.json
    out={
        "ok": True,
        "message": "Success",
        "new_id": user.insert(
            user_data.get("first_name"),
            user_data.get("last_name"),
            user_data.get("hobbies")
        )
    }
    return out, 201