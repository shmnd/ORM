


# ////////////////////////////////////////////////////////////topics answer link chat gpt//////////////////////////////////////////////////////////

# https://chat.openai.com/share/af936496-020e-4d54-8ae1-fd81676999d9

# ////////////////////////////////////////////////////////////topics//////////////////////////////////////////////////////////

# last()
# first()

# ● Get
# ● Filter
# ● Q object
# ● Annotate vs Aggregate
# ● Values and Values list
# ● F and FO object
# ● Managers
# ● Types of model inheritance in Django
# ● Meta class attributes
# ● Prefetch related and Select related
# ● Signals
# ● Raw method
# ● Curser
# ● Redirect and Reverse lazy
# ● Aggregate functions
# ● Bulk cerate
# ● exclude()
# ● Month, year, weekday , day
# ● Contains, icontains
# ● Abstract user and abstract base user

# Pending Topics:
# Use of custom managers
# Reverse vs reverse lazy
# Abstract user vs abstract base user - concept not clear 
# Signals
# Select related and prefetch related -  concept not clear
# Bulk create


# ///////////////////////////////////////basics things////////////////////////////////////////////////////////////

# orm shells

# py manage.pys shell

# cd orm

# from orange.models import employee

# To insert a data 
# emps=employee.objects.create(name='eldhose',age=21,place='wayanad',gender='male',salary=25000) 

# emps.save()

# emps=employee.objects.all()


# >>> for i in emps:
# ...     print(i.name,i.age,i.gender,i.rplace,i.salary)

# (press 2 enter to run)

# output:-

# Car Plascott 1 Male california 55764
# Ricki Shemwell 2 Female usa 70638
# Spense Kensett 3 Male germany 87168
# Tisha Coushe 4 Genderfluid lodon 50208
# Car Plascott 1 Male california 55764
# Ricki Shemwell 2 Female usa 70638
# Spense Kensett 3 Male germany 87168
# Tisha Coushe 4 Genderfluid lodon 50208
# Car Plascott 1 Male california 55764
# Ricki Shemwell 2 Female usa 70638
# Spense Kensett 3 Male germany 87168
# Tisha Coushe 4 Genderfluid lodon 50208
# eldhose 21 male wayanad 25000

# To delete all value 
# emp=employee.objects.all()
# >>> emp.delete() 
# (175, {'orange.employee': 175})

# bulk create
# >>> new=[employee(name='eldhose',age=21,gender='male',place='manjeri',salary=45000),empl
# oyee(name='raheem',age=21,gender='male',place='wayanad',salary=50000)]
# >>> employee.objects.bulk_create(new)


# to update

# up=employee.objects.get(name='shamnad')
# up.salary=70000
# up.save()


# update on specific condition
# # Suppose you want to update the salaries for all employees in 'New York'
# Employee.objects.filter(location='New York').update(salary=60000.00)


# A Q object is a powerful tool in Django ORM that allows you to perform complex queries with less and simple code. It is an object that encapsulates a collection of keyword arguments, which are specified as in Field lookups above. Q objects can be used for both filtering and exclusion queries.
# For example, if you want to return all objects that have a field named 'name' that starts with 'John' or 'Jane', you can use the following Q object:
# from django.db.models import Q

# Q(name__startswith='John') | Q(name__startswith='Jane')
# Use code with caution.
# Learn more
# You can also use Q objects to combine multiple conditions using logical operators such as AND and OR. For example, if you want to return all objects that have a field named 'age' that is greater than 30 and a field named 'gender' that is equal to 'male', you can use the following Q object:
# Q(age__gt=30) & Q(gender='male')
# Use code with caution.
# Learn more
# Q objects are a very powerful tool that can be used to simplify complex queries. If you find yourself writing complex queries, it is worth considering using Q objects to make your code more readable and maintainable.

# >>> from django.db.models import Q
# >>> set=Q(name__istartswith='s') & Q(age=30)
# >>> res=students.objects.filter(set) 
# >>> for i in res:
# ...     print(i.name) 
# ...
# shamnad
# sabeeh
