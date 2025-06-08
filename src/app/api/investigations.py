from flask import Blueprint, request, jsonify, abort
from typing import List
from uuid import UUID

from ..models import Investigation
from ..services.store import InvestigationStore
from ..services.auth import get_current_user, User
from ..services.watermark import add_watermark

investigations_bp = Blueprint('investigations', __name__)

store = InvestigationStore()

@investigations_bp.route('/investigations', methods=['POST'])
def create_investigation():
    user = get_current_user()
    data = request.get_json(force=True)
    inv = Investigation(**data)
    inv = store.create(inv, user)
    return jsonify(add_watermark(inv.dict(), user))

@investigations_bp.route('/investigations/<uuid:inv_id>')
def get_investigation(inv_id: UUID):
    user = get_current_user()
    inv = store.get(inv_id, user)
    if not inv:
        abort(404)
    return jsonify(add_watermark(inv.dict(), user))

@investigations_bp.route('/investigations')
def list_investigations():
    user = get_current_user()
    invs = store.list(user)
    return jsonify([add_watermark(inv.dict(), user) for inv in invs])

