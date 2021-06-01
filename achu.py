# importing the module
import csv
import sys
def topper_find(d):
	m = max(d)
	indices=[i for i, j in enumerate(d) if j == m]
	return indices
def topper_print(s,list1):
	if len(list1)==1:
		for i in list1:
			print("Topper in",s,"is",name[i])
	else:
		print("The toppers in",s,"are")
		for i in list1:
			print(name[i])
def total_finder(m,b,e,p,c,h):
	n=[]
	index_list=[]
	x=range(0,len(m))
	for i in x:
		s=int(m[i])+int(b[i])+int(e[i])+int(p[i])+int(c[i])+int(h[i])
		n.append(s)
	demo_sum=n.copy()
	demo_sum.sort(reverse=True)
	for i in range(0,3):
		index_list.append(n.index(demo_sum[i]))
	return index_list
fname= sys.argv[1]
filename = open(fname, 'r')
file = csv.DictReader(filename)
name = []
maths = []
biology = []
english = []
physics = []
chemistry = []
hindi = []
top3=[]
for col in file:
	name.append(col['Name'])
	maths.append(col['Maths'])
	biology.append(col['Biology'])
	english.append(col['English'])
	physics.append(col['Physics'])
	chemistry.append(col['Chemistry'])
	hindi.append(col['Hindi'])
index=topper_find(maths)
topper_print("Maths",index)
index=topper_find(biology)
topper_print("Biology",index)
index=topper_find(english)
topper_print("English",index)
index=topper_find(physics)
topper_print("Physics",index)
index=topper_find(chemistry)
topper_print("Chemistry",index)
index=topper_find(hindi)
topper_print("Hindi",index)
ind=total_finder(maths,biology,english,physics,chemistry,hindi)
for i in range (0,len(ind)):
	top3.append(name[ind[i]])
print("The best students in the class are",(top3[0],top3[1],top3[2]))
#print(chemistry)
#print(hindi)
#print(name)
#print(maths)
#print(biology)
#print(english)
#print(physics)
