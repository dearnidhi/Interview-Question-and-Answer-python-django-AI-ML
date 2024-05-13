

"""Context managers are a great tool for resource management. 
They allow you to allocate and release resources precisely when you want to.
 A well-known example is the with open() statemtent:

"""
with open('notes.txt', 'w') as f:
    f.write('some todo...')

    f = open('notes.txt', 'w')
try:
    f.write('some todo...')
finally:
    f.close()


    """Examples of context managers
Open and close files
open and close database connections
Acquire and release locks:"""
from threading import Lock
lock = Lock()

# error-prone:
lock.acquire()
# do stuff
# lock should always be released!
lock.release()