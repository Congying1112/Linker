#coding=utf-8

def LoadArticles():
	id = 1;
	articles = []
	#
	art = ClsArticle(id, "第一篇叽歪", "2014-06-24 19:00:18")
	art.add_tag("jiwai")
	art.add_p("终于有个不是很像样但总归是完完全全属于自己的窝了。")
	art.add_p("过年的时候就开始有搭窝的想法到现在才有这么个不像样的东西，强烈鄙视一下自己的执行力。")
	art.add_p("以下是反省：")
	art.add_p("总想着先把窝搭起来，然后再填东西，很多想法没有记下来，前段时间一直纠结于整个网站该怎么设计，各种折腾各种不满意，不干正经事，净干些有的没的只看得到浪费的时间完全看不到产出的事，遍地都是无用功。")
	art.add_p("以下是反反省(人的脸皮要不要这么厚)")
	art.add_p("鉴于女生总是对自己的窝有天然的情结，无论神经多大条，所以不管在这上面花多少心思都是可原谅的不是么，于是姐姐就权且把你当做个妹子然后原谅你啦:)另外，还有个更冠冕堂皇又事实上还是比较正确的理由是：不折腾怎么知道到底想要啥，类似于折腾一圈高端洋气的记录工具、管理工具之后，最终还是返朴归真回归txt的怀抱。道理都是一样一样滴~~这么有哲理，好想给自己颁个奖~~")
	art.add_p("从有搭窝想法开始就一直在yy搭完窝以后的幸福生活，其实也无非是可以喝着不管什么反正顺口的东西，窝在自己那个柠檬布丁里，晒着暖乎乎的大太阳，然后或是梳理自己的一路走来，把它们一件件布置到窝里，或是娓娓道来当下的事当下的心情，又或是捣鼓一些很酷很好玩的事，一点点去完成自己一直以来的那个梦想，这是我现阶段能想到的最惬意的人生了。")
	art.add_p("作为首篇，说点不是很正事的正事吧~")
	art.add_p("Why here?")
	art.add_p("就像子标题写的，“找个地方跟自己扯扯淡，顺便让小日子有迹可循”，虽然微博、微信、人人，甚至QQ空间都有这功能，但人多人杂，所有人看所有人罢了，很多东西也并不想公诸于众，找个清净的地儿，用心经营这个虚拟的家，大门又是敞开的，爱来的主儿得空过来坐坐聊聊，不爱来的也就落得耳根子清静，多好。")
	art.add_p("此为初衷，过个一年再回头看看演变成啥样了...")
	art.add_p("Why Elaine?")
	art.add_p("出处是个人看的为数不多的偶像剧之一《命中注定我爱你》。契机是13年入职新公司买了新本本需要输入用户名，那个刹那突然有个念头，那么就从这个用户名开始新生活吧。一直以来，自己骨子里的性格跟主人公比较像，也很欣赏欣怡最后的蜕变，希望自己经历那件事之后也可以完成跟她一样的蜕变，也很希望可以跟她一样幸运有一双强有力的手出现把我拉出泥潭，这可能也是有生以来最期待有那么一个人出现的时间段了，但内心非常清楚这些总归是偶像剧里才容易出现的桥段，只是话说回来，相较于有这么个人拉我，完全靠着自己的力量爬出泥潭对自己内心的锻炼应该是更大一些，毕竟生命中总是有些路需要自己一个人走过来的。至于另一个愿望，现在看来，勉强也算及格喽。")
	art.add_p("Why Abumiao?")
	art.add_p("养的一只傻猫，原本以为傻猫跟了我是傻猫的福气，各种宠着各种护着各种心疼，无比强大的容忍度，然后...anyway，谨以这种方式念叨我的傻猫。")
	art.add_p("What to do?")
	art.add_p("三大块：学习向、生活向、工作向；互相之间又有交集，各种攒经验，各种记录。")
	art.add_p("好啦，迈出了第一步，接下来就是慢慢迭代慢慢积累了喽 O(∩_∩)O~")
	art.add_p("By the way，老妈生日快乐:)")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "关于blog的YY", "2014-06-25 21:04:18")
	art.add_tag("yy")
	art.add_tag("blog")
	art.add_p("火车上关于博客内容yy了一些东西，记录下：")
	art.add_p("1. 文章不预先分类，只贴标签，可以多个，文章包括新写的和搬运过来的")
	art.add_p("2. 系统自动分类并展示")
	art.add_p("3. 文章分析，所有文章、按各种维度分类(时间轴横向、纵向，天气，等等能想到的)，看看自己脑子里到底都在想些什么...")
	art.add_p("这就好多事啦，粗粗一看，就涉及分类算法、中文分词、语义分析三个玩意了，还不包括前端展示。Hoho，ms很高端的样子，其实可以做得很傻...迫不及待准备动手喽~这磨刀霍霍的小样(*/ω＼*)")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "当前遇到的几个问题", "2014-06-25 21:04:18")
	art.add_tag("problem")
	art.add_p("1. 手贱装了wordexpress、nginx、mysql，卸不干净...nginx每次开机自启动地很嗨皮")
	art.add_p("2. 手动启动flask之后，总是时不时自己会断掉，不晓得是不是跟nginx有关系，一失手成千古恨啊")
	art.add_p("3. python传中文字符给前端ok，但是前端要显示的话就跪了，错误提示：Internal Server Error[The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.]。综上，可得，当前界面所有的中文都是静态的...所以，请尽情鄙视...")
	art.add_p("ps:嗯，问题列表可以作为一个单独的分类")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "九宫", "2014-06-26 06:34:12")
	art.add_tag("emotion")
	art.add_p("请诚实面对自己，有些事该承认的还是要承认的，怕顶个什么用啊亲，跟个鸵鸟似的。就是承认了又能怎么样呢，既然都是鸵鸟了，还不是尽给自己找不痛快...")
	art.add_p("转移注意力，其实前两天做得还可以，如果今天身体没有提醒自己的话，继续加油吧。")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "模板传中文变量前端显示时报错问题closed", "2014-06-26 11:16:57")
	art.add_tag("problem")
	art.add_p("1. python文件首行添加：#coding=utf-8")
	art.add_p("2. jinja模板中处：{{中文变量名.decode('utf8')}}")
	art.add_p("都要这么设吗？ms稍显麻烦啊。不晓得还有没有其他更方便的办法")
	articles.insert(0,art)
	#
	id = id + 1
	art = ClsArticle(id, "catagory,article类封装", "2014-06-26 11:23:57")
	art.add_tag("site_timeline")
	art.add_p("将类别和文章封装成类，接下去持久化去搞个简单的数据库")
	articles.insert(0,art)
	#
	"""id = id + 1
	art = ClsArticle(id, "第一篇叽歪", "2014-06-26")
	art.add_tag("")
	art.add_p("")
	articles.insert(0,art)"""
	#
	return articles

class ClsArticle(object):
	"""docstring for ClsArticle"""
	def __init__(self, id, title, datetime):
		super(ClsArticle, self).__init__()
		self.id = "article_" + bytes(id)
		self.title = title
		self.datetime = datetime
		self.para_list = []
		self.tag_list = []
	def add_p(self, para):
		self.para_list.append(para)
	def add_tag(self, tag):
		self.tag_list.append(tag)
	def get_article(self):
		return self.para_list;