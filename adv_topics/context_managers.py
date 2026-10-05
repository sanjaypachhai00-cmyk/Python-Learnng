#Context managers power the with statement.
#  They guarantee setup and cleanup — even when exceptions happen.


# file is automatically closed here, even if an exception occurred

# The with block calls two methods on the object:
# __enter__ — runs at the start
# __exit__ — runs at the end (always, even on exceptions)


#eg.
with open("hello.txt","w")as file:
    file.write("Hello Sujata")



#context lib
from contextlib import contextmanager
@contextmanager
def my_context():
    print("Entering")
    yield
    print("Exiting")
with my_context():
    print("Inside context")


#exception
@contextmanager
def suppress_and_log():
    try:
        yield
    except ValueError as e:
        print(f"Swallowed: {e}")
        # NOT re-raising → exception is suppressed
with suppress_and_log():
    raise ValueError("boom")
print("Continued")


#timing
import time
from contextlib import contextmanager
@contextmanager
def timer(label="block"):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label}: {time.perf_counter() - start:.4f}s")
with timer("loading"):
    time.sleep(0.5)



#locking
import threading
from contextlib import contextmanager

lock = threading.Lock()

@contextmanager
def locked(l):
    l.acquire()
    try:
        yield
    finally:
        l.release()

with locked(lock):
    # critical section
    ...