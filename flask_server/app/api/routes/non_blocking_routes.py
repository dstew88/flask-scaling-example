
from ..tasks.blocking_task import blocking
from flask import Blueprint

bp = Blueprint("non-blocking", __name__)


@bp.route("/", methods=["GET"])
def non_blocking():

    task = blocking.delay(10)

    return {
        "type": "non-blocking",
        "complete": True
    }
