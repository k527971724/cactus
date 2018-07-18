from app.models import Article
file_handle = open("2.txt", encoding="UTF8")
body_html = file_handle.read()
file_handle.close()
tmp = Article(title="标题不明")
tmp.body_html = body_html
tmp.recommend01 = 3
tmp.recommend02 = 3
tmp.recommend03 = 3
tmp.recommend04 = 3
tmp.recommend05 = 3
tmp.recommend06 = 3

file_handle = open("3.txt", encoding="UTF8")
body_html = file_handle.read()
file_handle.close()
tmp2 = Article(title="无题")
tmp2.body_html = body_html
tmp2.recommend01 = 1
tmp2.recommend02 = 1
tmp2.recommend03 = 1
tmp2.recommend04 = 1
tmp2.recommend05 = 1
tmp2.recommend06 = 1

