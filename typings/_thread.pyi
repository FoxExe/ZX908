"""
Function:
_thread module contains features related to thread operations, and provides methods for creating and deleting threads, and interfaces related to mutex and semaphore.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/stdlib/_thread.html
"""


def get_ident():
    """Requires the current thread number.

    @return: Returns the current thread number.
    """

def stack_size(size):
    """ set thread stack size
    Setting or getting the stack size which is used to create a thread (Unit: byte) depends on whether size is provided. The stack size is 8448 bytes by default, with a minimum of 8192 bytes.

    @param size: Sets the stack size which is used to create a thread when size is provided.
    @return: Returns the stack size which is used to create a thread when size is not provided.
    """

def start_new_thread(function, args):
    """create new thread.
    Creates a thread to receive the executing function and the parameter of the executed function, and passes an empty tuple if function has no parameters.

    @param function: The executing function of the thread.
    @param args: The parameter of the executing function of the thread, which passes an empty tuple when the function has no parameters.
    @return: Returns the ID of the created thread.
    """

def threadIsRunning(thread_id):
    """check if thread is running or not according to `thread_id`.

    :param thread_id: thread ident, a int type.
    :return: True or False
    """

def stop_thread(thread_id):
    """Deletes a thread. The main thread cannot be deleted.

    @param thread_id: The returned ID when the thread is created. If the value is 0, the current thread is deleted.
    @return: None
    """

def get_heap_size():
    """Gets the remaining size of heap in the system.

    @return: Returns the remaining size of heap in the system. (Unit: byte)
    """

class Lock(object):

    def acquire(self):
        """Acquires the lock.

        @return: True-Successful execution; False-Failed execution.
        """

    def release(self):
        """Releases the lock."""

    def locked(self):
        """Returns the status of the lock.

        @return: True indicates the status of the lock has been required by some thread; False indicates the status of the lock has not been required by the thread.
        """

def allocate_lock() -> Lock:
    """Creates a mutex object.

    @return: Returns the created mutex object.
    """

def delete_lock(lock):
    """Deletes the created mutex.

    @param lock: The returned mutex object when the mutex is created.
    @return: None
    """

class Semphore(object):


    def acquire(self):
        """Acquires the semphore."""

    def release(self):
        """Releases the semphore."""

    def getCnt(self):
        """Gets the maximum value of the semaphore count and the current remaining count value.

        @return: (maxCnt, curCnt)-tuple: maxCnt is the maximum count value, and curCnt is the current remaining count value.
        """

def allocate_semphore(initcount) -> Semphore:
    """Creates a semphore object.

    @param initcount: The initial count value and also the maximum value of the semaphore.
    @return: Returns the created semphore object.
    """

def delete_semphore(semphore):
    """Deletes the created semphore.

    @param semphore: The returned semphore object when the semphore is created.
    @return: None
    """
