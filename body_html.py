from app.models import Article
file_handle = open(r"C:\Users\knight\Desktop\1.txt", encoding="UTF8")
body_html = file_handle.read()
file_handle.close()
tmp = Article(title="手机")
tmp.body_html = body_html
tmp.recommend01 = 2
tmp.recommend02 = 2
tmp.recommend03 = 2
tmp.recommend04 = 2
tmp.recommend05 = 2
tmp.recommend06 = 2
