#!/usr/bin/python
# -*- encoding: iso-8859-1 -*-

inf = open("train.txt", "r")
content_list = inf.readlines()
#print(content_list[4])

for num in 250, 500, 750:
    outf = open("train" + str(num) + ".txt", "w")
    with outf as f:
        for item in content_list[0:num - 1]:
            f.write("%s" % item)
    outf.close()