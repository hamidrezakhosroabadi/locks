from retry.api import retry_call


class Lock:
    """
    A lock management class that provides a context manager for acquiring and releasing locks using a specified driver.

    Locks can be acquired and released using the `try_acquire_lock` and `try_release_lock` methods respectively. The
    lock acquisition and release operations are retried based on the provided retry options.

    Example:
        driver = RedisDriver(host='localhost', port=6379)
        lock_key = 'my_lock'
        retry_options = {'tries': 3, 'delay': 1}

        with Lock(driver, lock_key, **retry_options):
            # Perform operations while holding the lock

    Attributes:
        __driver: The driver instance used for acquiring and releasing locks.
        __key: The key associated with the lock.
        __retry_options: Additional options passed to the retry_call function.
    """

    def __init__(self, driver, key, **retry_options):
        """
        Initializes a Lock instance with the provided driver, key, and retry options.

        Args:
            driver: An instance of the lock driver implementing the DriverInterface.
            key: The key associated with the lock.
            retry_options: Additional options passed to the retry_call function.
        """
        self.__driver = driver
        self.__key = key
        self.__retry_options = retry_options

    def try_acquire_lock(self, key) -> None:
        """
        Attempts to acquire the lock based on the provided key.

        Args:
            key: The key used for acquiring the lock.

        Raises:
            AcquireLockException: If an error occurs while acquiring the lock.
        """
        retry_call(self.__driver.acquire_lock, fargs=[key], **self.__retry_options)

    def try_release_lock(self, key) -> None:
        """
        Attempts to release the lock based on the provided key.

        Args:
            key: The key used for releasing the lock.

        Raises:
            ReleaseLockException: If an error occurs while releasing the lock.
        """
        retry_call(self.__driver.release_lock, fargs=[key], **self.__retry_options)

    def __enter__(self) -> None:
        """
        Acquires the lock when entering a context managed block.

        The lock acquisition is retried based on the provided retry options.
        """
        self.try_acquire_lock(self.__key)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Releases the lock when exiting a context managed block.

        The lock release is retried based on the provided retry options.

        Args:
            exc_type: The type of the exception raised, if any.
            exc_val: The value of the exception raised, if any.
            exc_tb: The traceback of the exception raised, if any.
        """
        self.try_release_lock(self.__key)
