import itchat
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import re
import jieba
import PIL.Image as Image
from wordcloud import WordCloud, ImageColorGenerator

def analyseProvince(friends):

    provlist = get_var('Province', friends)
    provdict = {}
    for p in provlist:
        provdict[p] = provdict.get(p,0) + 1
    provdict = sorted(provdict.items(), key= lambda x : x[1], reverse=True)

    #画图
    figpro = plt.figure(figsize=(10,5))
    axpro = figpro.add_subplot(111)
    axpro.set_title('省份')
    xticks = np.linspace(0.5,20,10)
    bar_width = 0.8
    pros= []
    values = []
    count = 0
    for d in provdict:
        pros.append(d[0])
        values.append(d[1])
        count += 1
        if count >= 10:
            break

    colors = ['#FFEC88', '#FFE4C4','#FFC125','#FFB6C1','#CDCDB4','#CDC8B1','#CDB79E','#CDAD00','#CD96CD',\
              '#CD853F']
    bars = axpro.bar( xticks, values, width=bar_width, edgecolor='none')
    axpro.set_ylabel('人数')
    axpro.set_xlabel('省份')
    axpro.grid()
    axpro.set_xticks( xticks)
    axpro.set_xticklabels(pros)
    axpro.set_xlim(0,20)
    axpro.set_ylim([0,100])

    for bar, color in zip( bars, colors):
        bar.set_color(color)
        height = bar.get_height()
        plt.text( bar.get_x()+bar.get_width()/4., height, '{}'.format(height))

    plt.show()

analyseProvince(friends)