import json
from app.models import Article
with open("last_list_1.json", 'r') as f:
    aa = json.load(f)  # 4500
    data = []

    for a in aa:
        tmp = Article()
        tmp.id = a['id']
        tmp.title = a['title']
        tmp.body = a['content']
        tmp.body_html = a['html']
        tmp.recommend01 = a['num1']
        tmp.recommend02 = a['num2']
        tmp.recommend03 = a['num3']
        tmp.recommend04 = a['num4']
        tmp.recommend05 = a['num5']
        tmp.recommend06 = a['num6']
        #print(a['id'])
        #print(tmp.id)
        data.append(tmp)
    #print("length" + str(len(data)))
    d_1000 = data[:1000]
    '''
    for d in data:
        print(str(d.id) + "  " + d.title)
    print(data[1365].id, data[1365].title)
    del data[1365]
    print(data[1365].id, data[1365].title)
    '''