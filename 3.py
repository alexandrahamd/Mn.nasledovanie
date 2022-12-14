class Employee:
    __slots__ = ('first', 'last', '__fullname', '__email')

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.__fullname = f'{self.first} {self.last}'
        self.__email = f"{self.first}.{self.last}@gmail.com"

    @property
    def fullname(self):
        return self.__fullname

    @fullname.setter
    def fullname(self, value):
        self.__fullname = value
        lst = value.split()
        self.first = lst[0]
        self.last = lst[1]

    @fullname.deleter
    def fullname(self):
        del self.__fullname

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value



emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# John
# John.Smith@email.com
# John Smith

emp_1.fullname = "Corey Schafer"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# Corey
# Corey.Schafer@email.com
# Corey Schafer

del emp_1.fullname
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# None
# None.None@email.com
# None None