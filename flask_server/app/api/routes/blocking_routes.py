from datetime import datetime
from flask import Blueprint

bp = Blueprint("blocking", __name__)


@bp.route("/", methods=["GET"])
def blocking():

    start = datetime.now().timestamp()
    while datetime.now().timestamp() < start + 10:
        # mimic a CPU intensive task
        continue

    print("Flask server instance completed blocking job", flush=True)

    return {
        "type": "blocking",
        "complete": True
    }
