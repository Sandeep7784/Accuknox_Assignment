from django.http import HttpResponse
from django.db import transaction
from .models import TestModel, TransactionTestModel
import time
import threading

#For Q1 and Q2
def test(request):
    start_time = time.time() #Setting the start time
    print(f"View running in thread: {threading.current_thread().name}") #Printing the thread name for the view
    TestModel.objects.create(name="Test Object")
    end_time = time.time() #Setting the end time
    
    execution_time = end_time - start_time #Calculating the execution time from start time and end time
    return HttpResponse(f"Execution time: {execution_time:.2f} seconds")

#For Q3
def transaction_test(request):
    try:
        with transaction.atomic():
            obj = TransactionTestModel.objects.create(name="Test Object") #This will try to create an object in the database
            return HttpResponse("Object created successfully")
    except Exception as e: 
        count = TransactionTestModel.objects.count()  #To check if the object was created or not by counting the objects
        return HttpResponse(f"Error occurred. Object count: {count}") #This will return 0 as the object was not created due to the exception raised by post_save signal