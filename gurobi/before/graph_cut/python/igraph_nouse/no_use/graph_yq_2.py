import sys
import time

from igraph import *

g = Graph();

# 4924 nodes in yq dataset Day1-1
g.add_vertices(4924);

# file = open("/home/yinhuan/gomory_yq_s.edgelist")
file = open("/home/yinhuan/pose_graph_yq_vis50.txt")

print('file open, adding edges')

for idx, v in enumerate(g.vs):
    v["name"] = idx

for line in file.readlines():
	line.strip('\n')	
	nums = line.split(" ")
	nums = [int(x) for x in nums ]
	# print(nums[0])
	g.add_edge(nums[0], nums[1], weight=nums[2])

file.close();


print('start gomory')
start = time.clock()

t = g.gomory_hu_tree(capacity="weight")

elapsed = (time.clock() - start)
print("Time used:",elapsed)



saveFile = open("/home/yinhuan/gomory_yq_vis50.txt", "w");

for e in t.es:
	saveFile.write(str(e.tuple[0])+' ')
	saveFile.write(str(e.tuple[1])+' ')
	saveFile.write(str(e["flow"])+'\n')

saveFile.close();

print('Finished Saving')
