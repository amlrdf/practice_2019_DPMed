import os
import pprint
pardir = 'data'
files = [os.path.join(pardir, fname)
         for fname in os.listdir(pardir)
         if os.path.splitext(fname)[1] == '.txt'] #主要为了选择file type去使用。如txt
#这是个逆向的执行过程，if --> for , then os.path....

files = []
for fname in os.listdir(pardir):
    if os.path.splitext(fname)[1] == '.txt':
        files.append(os.path.join(pardir, fname))

counts = {}
for file_ in files:
    with open(file_, 'r') as fh:  #打开txt文件,这段是非常经典的多文件读取方法，值得重视
        for line in fh:
            for word in line.split():
                counts[word] = counts.get(word, 0) + 1
# print(list(counts.values()))
# big_count = None
# big_word = None
# for word, count in counts.items():
#     if big_count is None or count > big_count:
#         big_word = word
#         big_count = count
#         print(big_word, big_count) #逐渐找出重复次数最大的string

tupple=[] #dictionary 是不能作为一个独立体系进行分类的。需要转换成[] i.e. list
for key, value in counts.items():
    tupple.append((key,value))
tupple.sort(key=lambda z:z[1])
pprint.pprint(tupple)
