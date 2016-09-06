# -*- coding: utf-8 -*-
import os
import sys

extens = [".py"]
linesCount = 0
filesCount = 0


def funCount(dirName):
    global extens, linesCount, filesCount
    for root, dirs, fileNames in os.walk(dirName):
        for f in fileNames:
            fname = os.path.join(root, f)
            try:
                ext = f[f.rindex('.'):]
                if (extens.count(ext) > 0):
                    filesCount += 1
                    l_count = len(open(fname).readlines())
                    print fname, " : ", l_count
                    linesCount += l_count
            except:
                pass


if len(sys.argv) > 1:
    for m_dir in sys.argv[1:]:
        print m_dir
        funCount(m_dir)
else:
    funCount(".")

print u'文件数目：', filesCount
print u'代码行数：', linesCount
