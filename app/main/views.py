from flask import render_template
from . import main  # 蓝本
# from .. import db
# from ..models import Article


# 【主页】
@main.route('/')
def index():
    return render_template('index.html')


# 【科技页面】
@main.route('/technology')
def technology():
    return render_template('technology.html')


# 【设计页面】
@main.route('/design')
def design():
    return render_template('design.html')


# 【人文页面】
@main.route('/humanity')
def humanity():
    return render_template('humanity.html')