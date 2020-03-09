from wordcloud import *
from jieba import *
from scipy.misc import imread

# 色调
# def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
#     # hset = randint(0,10)
#     # if hset > 5:
#     #     h = randint(0, 80)
#     # else:
#     #     h = randint(200, 255)
#     h = randint(0, 80)
#     s = int(100.0 * 255.0 / 255.0)
#     l = int(100.0 * float(randint(60, 120)) / 255.0)
#     return "hsl({}, {}%, {}%)".format(h, s, l)
# ,color_func = random_color_func

# 填充形状
mask = imread("wordclouddata/thechinamap.png")
f = open("test3.txt","r",encoding = "utf-8")
t = f.read()
f.close()
ls = lcut(t)
txt = " ".join(ls)
w = WordCloud(font_path = "msyh.ttc", mask = mask, width = 1000, height = 700, background_color = "white")
w.generate(txt)
w.to_file("test.png")