#call by reference
# def add(a):
#     a.append(5)
#     print(a)
#     print(id(a))
# a=[1,2,3]
# add(a)
# print(id(a))
# print(a)

#if we don't want to change the actual parameter when the formal parameter changes in call by reference
def sum(a):
    a=list(a)
    a[1]=5
    print(id(a))
    print(a)
a=[1,2,3]
sum(a)
print(a)
print(id(a))