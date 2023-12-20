from flask import Blueprint, render_template

bp = Blueprint('admin', __name__)

@bp.route('/admin')
def func():
    return render_template('admin.html')