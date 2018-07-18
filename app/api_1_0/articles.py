from flask import jsonify
from ..models import Article
from . import api


# 【一篇文章】
@api.route('/articles/<int:id>')
def get_article():
    article = Article.query.get_or_404(id)
    article01 = Article.query.get_or_404(article.recommend01)
    article02 = Article.query.get_or_404(article.recommend02)
    article03 = Article.query.get_or_404(article.recommend03)
    article04 = Article.query.get_or_404(article.recommend04)
    article05 = Article.query.get_or_404(article.recommend05)
    article06 = Article.query.get_or_404(article.recommend06)

    result = [{"title": article.title,
               "html": article.body_html,
               "title1": article01.title,
               "title2": article02.title,
               "title3": article03.title,
               "title4": article04.title,
               "title5": article05.title,
               "title6": article06.title,
               "id1": article.recommend01,
               "id2": article.recommend02,
               "id3": article.recommend03,
               "id4": article.recommend04,
               "id5": article.recommend05,
               "id6": article.recommend06,
               }]
    return jsonify(result)
