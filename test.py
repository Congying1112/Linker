from model import article

at = article.ClsArticle("title")
at.add_p("test1")
at.add_p("test2");

print at.get_article()