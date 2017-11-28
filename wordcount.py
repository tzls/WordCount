# encoding=utf-8
from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np
from numpy import unicode
from collections import OrderedDict

class WordCount(object):
    def wordcloudplot(self, txt):
        path ='C:/Users/zhou/PycharmProjects/WordCount/word_count/MSYH.TTF'
        alice_mask = np.array(PIL.Image.open('C:/Users/zhou/PycharmProjects/WordCount/word_count/1.png'))
        wordcloud = WordCloud(font_path=path,
                              background_color="black",
                              margin=5, width=1800, height=800, mask=alice_mask, max_words=2000, max_font_size=60,
                              random_state=42)
        wordcloud = wordcloud.generate_from_frequencies(txt)
        wordcloud.to_file('C:/Users/zhou/PycharmProjects/WordCount/word_count/she.jpg')
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.show()

    def test(self):
        a= OrderedDict([])
        f = open(r'C:\Users\zhou\PycharmProjects\WordCount\word_count\1.txt', 'r').read()
        words = list(jieba.cut(f))
        for word in words:
            if word in a:
                a[word] += 1
            else:
                a[word] = 1
        with open("2.txt","w") as f:
            for key in a.keys():
                f.write(key)
                f.write(str(a[key]))
        b = OrderedDict(sorted(a.items(), key=lambda x: x[1]))
        self.wordcloudplot(b)

if __name__=='__main__':
    wc= WordCount()
    wc.test()