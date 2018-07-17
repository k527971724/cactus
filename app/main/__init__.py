from flask import Blueprint

main = Blueprint('main', __name__)
# 蓝本名字和蓝本所在包的名字

from . import views, errors
# views，errors中引入了main蓝本，所以引入他们要放在main定义后
# PEP要求模块引入在代码顶部，此处无法符合PEP要求
