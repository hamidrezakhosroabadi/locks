class AcquireLockException(Exception):
    """
    An exception raised when acquiring a lock encounters an error.

    This exception is raised when there is an issue with acquiring a lock, typically used in concurrent programming
    to synchronize access to shared resources. It can be used to handle exceptional cases where acquiring the lock
    fails, such as timeouts or other errors.
    """
    pass


class ReleaseLockException(Exception):
    """
    An exception raised when releasing a lock encounters an error.

    This exception is raised when there is an issue with releasing a lock that has been previously acquired. In
    concurrent programming, locks are typically released to allow other threads or processes to access shared resources
    safely. If an error occurs during the release operation, this exception can be raised to handle exceptional cases.
    """
    pass
