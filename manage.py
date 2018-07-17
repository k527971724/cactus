import os
from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import Article

app = create_app('development')
manager = Manager(app)
migrate = Migrate(app, db)

@manager.shell
def make_shell_context():  # context的意思是上下文
    return dict(app=app, db=db, Article=Article)
    # 模型与实例在此添加，能在命令行当中使用


manager.add_command("server", Server())
# python manage.py server 运行服务器
manager.add_command("shell", Shell(make_context=make_shell_context ))
# python manage.py shell  运行命令行并进行默认导入
manager.add_command("db", MigrateCommand)
# python manage.py db     运行命令行并使用SQLAlchemy

# 运行当前文件：
if __name__ == '__main__':
    print("运行manage.py")
    manager.run()
