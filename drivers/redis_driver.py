from redis import Redis
from driver_exceptions import AcquireLockException, ReleaseLockException
from driver_interface import DriverInterface


class RedisDriver(DriverInterface):
    """
    A driver implementation for managing locks using Redis as the backend store.

    This driver utilizes the Redis client library for interacting with a Redis server, an in-memory data store. It
    implements the DriverInterface to provide methods for acquiring and releasing locks.
    """

    def __init__(self, **options):
        """
        Initializes an instance of RedisDriver.

        Parameters:
            **options: Additional options to be passed to the Redis client.

        Notes:
            This method initializes an instance of RedisDriver and establishes a connection to the Redis server using
            the provided options.
        """
        self.__connection = Redis(**options)

    def acquire_lock(self, key) -> None:
        """
        Acquires a lock based on the provided key.

        Parameters:
            key (str): The key used to acquire the lock.

        Raises:
            AcquireLockException: If an error occurs while acquiring the lock.

        Notes:
            This method attempts to acquire a lock by using the Redis client to set the value associated with the key
            only if the key does not already exist. If the key already exists, indicating that the lock is already held,
            an AcquireLockException is raised.
        """
        if not self.__connection.setnx(key, str()):
            raise AcquireLockException()

    def release_lock(self, key) -> None:
        """
        Releases a lock based on the provided key.

        Parameters:
            key (str): The key used to release the lock.

        Raises:
            ReleaseLockException: If an error occurs while releasing the lock.

        Notes:
            This method releases a lock by deleting the key from the Redis server using the Redis client. If the delete
            operation fails, indicating an error in releasing the lock, a ReleaseLockException is raised.
        """
        if not self.__connection.delete(key):
            raise ReleaseLockException()
