from flask import Blueprint, render_template

isihome_bp = Blueprint('isihome', __name__)

@isihome_bp.route('/isihome')
def isihome():
    return render_template('isihome.html')