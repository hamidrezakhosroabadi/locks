class DriverInterface:
    """
    An interface for managing locks based on keys.
    
    This interface defines methods for acquiring and releasing locks based on a provided key. Implementations of this
    interface should provide concrete implementations for these methods to handle the actual locking mechanism.
    """

    def acquire_lock(self, key: str) -> None:
        """
        Acquires a lock based on the provided key.

        Parameters:
            key (str): The key used to acquire the lock.

        Raises:
            AcquireLockException: If an error occurs while acquiring the lock.

        Notes:
            This method should be implemented to handle the logic of acquiring a lock based on the provided key.
            Locks are typically used in concurrent programming to synchronize access to shared resources. If an error
            occurs during the acquisition of the lock, an AcquireLockException should be raised.
        """
        pass

    def release_lock(self, key: str) -> None:
        """
        Releases a lock based on the provided key.

        Parameters:
            key (str): The key used to release the lock.

        Raises:
            ReleaseLockException: If an error occurs while releasing the lock.

        Notes:
            This method should be implemented to handle the logic of releasing a lock based on the provided key.
            Locks are typically released to allow other threads or processes to access shared resources safely. If an
            error occurs during the release of the lock, a ReleaseLockException should be raised.
        """
        pass
