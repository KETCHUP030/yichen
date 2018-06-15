import itchat
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import re
import jieba
import PIL.Image as Image
from wordcloud import WordCloud, ImageColorGenerator


def drawWordcloudPlot(counts):
    coloring = np.array(Image.open("E:/baidupic/alice_color.png"))
    wc = WordCloud(background_color="white",
                   max_words=2000,
                   mask=coloring,
                   max_font_size=60,
                   random_state=42,
                   scale=2,
                   font_path="c:/Windows/Fonts/SimHei.ttf")
    wc.generate_from_frequencies(counts)
    image_colors = ImageColorGenerator(coloring)

    plt.imshow(wc)
    plt.axis("off")
    plt.savefig('friendSign.jpg')
    plt.show()


def analyseSignature(friends):
    signatures = get_var('Signature', friends)
    siglist = []
    for sign in signatures:
        sign = sign.strip().replace("span", "").replace("class", "").replace("emoji", "")
        rep = re.compile("lf\d+\w*|[<>/=]")
        sign = rep.sub("", sign)
        siglist.append(sign)
    text = "".join(siglist)
    wlist = jieba.cut(text, cut_all=True)
    counts = {}
    for word in wlist:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    wdict = {}
    for d in counts.items():
        if d[1] > 2:
            wdict[d[0]] = d[1]

    drawWordcloudPlot(wdict)

analyseSignature(friends)