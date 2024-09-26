from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
import threading

class TestModel(models.Model): #Model for testing the signals for Q1 and Q2
    name = models.CharField(max_length=100)

class TransactionTestModel(models.Model): #Model for testing the signals for Q3
    name = models.CharField(max_length=100)

@receiver(post_save, sender=TestModel)
def slow_signal(sender, instance, created, **kwargs): #For demonstrating synchronous behavior (Q1)
    time.sleep(5)  #Added the sleep time of 5 seconds to simulate a slow signal
    print(f"Signal completed for {instance.name}") 

@receiver(post_save, sender=TestModel)
def thread_signal(sender, instance, created, **kwargs): #For demonstrating same-thread execution for Q2
    time.sleep(1)  #Added the small delay to ensure we can capture the thread
    print(f"Signal running in thread: {threading.current_thread().name}") #Printing the thread name for the signal for Q2 and comparing it with the view thread

@receiver(post_save, sender=TransactionTestModel) 
def transaction_signal(sender, instance, created, **kwargs): #For demonstrating transactional behavior (Q3)
    if created:
        raise Exception("Simulated error in signal") #This will raise an exception to simulate an error in the signal for Q3