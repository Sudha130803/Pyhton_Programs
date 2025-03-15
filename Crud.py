a=[
    {
        "id":1,
        "name":"sudha",
        "age":20
    },
    {
        "id":2,
        "name":"jaanu",
        "age":22
    }
]

def create(list,payload):
    list.append(payload)
    return list 

def getAll(list):
    return list

def getOne(list,id):
    for i in list:
        if i["id"]==id:
            return i
        
def update(list,id,updatePayload):
    for i,item in enumerate(list):
        if item["id"]==id:
            list[i]={**item,**updatePayload}
            return list
    return list

def delete(list,id):
    for i,item in enumerate(list):
        if item["id"]==id:
            del list[i]
            return list
    return list

# print(a)
b={"id":"3","name":"vimal","age":"30"}
print(create(a,b))
# print(getAll(a))
print(getOne(a,2))
item={"name":"mythili"}
print(update(a,2,item))
print(delete(a,2))



