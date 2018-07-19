import json
from app.models import Article
with open("last_list_1.json", 'r') as f:
    aa = json.load(f)  # 4500
    tmp = Article()
    for a in aa:


    # 测试只写入一篇文章

