# Django Signals Assignment

## Overview

This assignment demonstrates three key concepts about Django Signals:

1. **Synchronous vs. Asynchronous execution of signals**.
2. **Thread behavior of signals**.
3. **Transaction behavior of signals**.

It also includes a Python class (`Rectangle`) to demonstrate how custom classes can be made iterable in Python.

## Project Setup

### Clone the Repository

To clone this repository, run the following command:

```bash
git clone https://github.com/Sandeep7784/Accuknox_Assignment.git
```
Navigate to the `assignment` directory
```bash
cd assignment
```

### Install Dependencies

It's recommended to use a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # This for Windows. On Unix/Linux use `source venv/bin/activate`
pip install -r requirements.txt
```

### Migrations

Run the following commands to set up the database:

```bash
python manage.py makemigrations questions
python manage.py migrate
```

### Running the Server

Start the Django development server with:

```bash
python manage.py runserver
```

## URL Endpoints

- **`/test/`**: Triggers the `post_save` signal for `TestModel` to test Q1 and Q2 (synchronous execution and thread behavior).
- **`/transaction-test/`**: Triggers the `post_save` signal for `TransactionTestModel` to test Q3 (transaction behavior).

## Answers to Questions

### Q1: Are Django signals executed synchronously or asynchronously?

By default, Django signals are executed synchronously. <br>
**Explanation:**
Synchronous execution means that when a signal is sent, the program waits for all receivers of that signal to complete their tasks before proceeding to the next line of code. In our code example, we created a signal that artificially delays execution for 5 seconds (using `time.sleep(5)`).

#### Output

```bash
Execution time: 6.49 seconds
```

**Conclusion:** The execution time indicates that the main thread waits for the signal to finish. If signals were asynchronous, the object creation would have completed almost instantly, while the signal would run in the background. It's important to note that while the output shows **6.49 seconds**, the exact execution time can vary but will generally be greater than **5 seconds** due to the synchronous nature of the signals.

### Q2: Do Django signals run in the same thread as the caller?

Yes, Django signals run in the same thread as the caller. </br>
**Explanation:**
A thread in programming is like a worker in a factory. Multiple threads can work simultaneously on different tasks. If signals ran in a different thread, they could potentially operate at the same time as the code that triggered them. <br>
Our code demonstrates that they run in the same thread by printing the name of the current thread both in the view (which triggers the signal) and in the signal itself.

#### Output

```bash
View running in thread: Thread-3 (process_request_thread)
Signal completed for Test Object
Signal running in thread: Thread-3 (process_request_thread)
```

**Conclusion:** The identical thread names printed for both the view and the signal confirm they are executed in the same thread context. It's worth mentioning that while the thread name (e.g., **Thread-3**) can vary across different runs, the important aspect is that both the view and the signal share the same thread identifier.

### Q3: Do Django signals run in the same database transaction as the caller?

Yes, by default, Django signals run in the same database transaction as the caller. </br>
**Explanation:**
A database transaction is a sequence of database operations that are treated as a single unit of work. If any part of the transaction fails, the entire transaction is rolled back (undone). <br>
Our code illustrates this behavior by creating a signal that deliberately raises an exception. We attempt to create an object inside a transaction, which triggers this signal. If the signal were not part of the same transaction, the object would be created despite the error in the signal.

#### Output

```bash
Error occurred. Object count: 0
```

**Conclusion:** The output indicates that when the signal raises an exception, the object is not created, resulting in a count of zero. This confirms that the signal is part of the same transaction, as the failure of the signal prevents the creation of the object.

## Python Custom Class: Rectangle

In addition to Django Signals, a custom iterable class `Rectangle` was created. The class is initialized with a length and width, and when iterated over, it yields these dimensions in the format `{'length': value}` and `{'width': value}`.

### Example:

```bash
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

#Example
rect = Rectangle(8, 4)
for dimension in rect:
    print(dimension)
```

### Output:

```bash
{'length': 8}
{'width': 4}
```
