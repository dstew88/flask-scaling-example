
from ..task_workers.blocking_task_worker import blocking
from flask import Blueprint

bp = Blueprint("non-blocking", __name__)


@bp.route("/", methods=["GET"])
def non_blocking():

    task = blocking.delay()

    return {
        "type": "non-blocking",
        "complete": True
    }
