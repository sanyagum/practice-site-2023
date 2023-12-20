from flask import Blueprint, render_template

bp = Blueprint('feedback', __name__)

@bp.route('/feedback')
def feedback():
    return render_template('feedback.html')