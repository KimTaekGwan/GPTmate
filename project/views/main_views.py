# myproject/sesac/views/post_views.py
from flask import url_for, request, redirect, Blueprint, render_template
from project.conn.db import db

import os

bp = Blueprint('main_views', __name__, url_prefix='/')

path_data = '../data'

@bp.route('/')  
def main():
    return render_template("pages/main.html")  
    # return redirect(url_for('main_views.upload'))

