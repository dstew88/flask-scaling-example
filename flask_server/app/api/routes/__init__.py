from flask import Blueprint

from .blocking_routes import bp as blocking_bp
from .non_blocking_routes import bp as non_blocking_bp

bp = Blueprint("api", __name__)

bp.register_blueprint(blocking_bp, url_prefix="/blocking")
bp.register_blueprint(non_blocking_bp, url_prefix="/non-blocking")
