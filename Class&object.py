# Class & Object:
# class first:
#     x=10
# n=first()
# print(n.x)

# class first:
#     def __init__(self, a,b):
#         self.c=a*b
#     def __str__
# n=first(2,3)
# print(n.c)

# class Emp():
#     def __init__(self, id, name, Add):
#         self.id = id
#         self.name = name
#         self.Add = Add

# class Freelance(Emp):
#     def __init__(self, id, name, Add, Emails):
#         super().__init__(id, name, Add)
#         self.Emails = Emails

# Emp_1 = Freelance(103, "Suraj kr gupta", "Noida" , "KKK@gmails")
# print('The ID is:', Emp_1.id)
# print('The Name is:', Emp_1.name)
# print('The Address is:', Emp_1.Add)
# print('The Emails is:', Emp_1.Emails)


class Add:
    def __init__(self,a):
        self.a=a
    def __eq__(self, obj2):
        return self.a==obj2
obj=Add(1)
obj2=Add(1)
print(obj==obj2)
print(obj is obj2)
print(obj.__eq__(obj2))