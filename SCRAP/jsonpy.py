import json
from appy import *	
# Data to be written
dictionary ={
"id": "04",
"name": "sunil",
"department": "HR"
}
	
# Serializing json
course=Courseadd.query.all()
l1,l2=[],[]
for i in course:
          l1.append(i.name)
          l2.append(i.semisters)
          
all_courses=dict(zip(l1,l2))

for i,j in all_courses.items():
          print(i,j)
          
json_object = json.dumps(all_courses, indent = 4)
print(json_object)




