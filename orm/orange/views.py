from django.shortcuts import render
from.models import employee



# # Create your views here.
 
# def employees(request):
#     ah=employee.objects.all()
    
#     sahal = [
#         employee(name="Car Plascott", gender="Male", age=1, salary=55764,place='california'),
#         employee(name="Ricki Shemwell", gender="Female", age=2, salary=70638,place='usa'),
#         employee(name="Spense Kensett", gender="Male", age=3, salary=87168,place='germany'),
#         employee(name="Tisha Coushe", gender="Genderfluid", age=4, salary=50208,place='lodon')
#     ]
#     s = employee.objects.bulk_create(sahal) 

#     context={'ah':ah}
#     return render(request,'test.html',context)
    

    
    #     import os


    
    
# my_instance = MyModel.objects.filter(name='example').order_by('some_field').first()


# import os

# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# clear_screen()