from etcd3 import client
from driver_exceptions import AcquireLockException, ReleaseLockException
from driver_interface import DriverInterface


class ETCDDriver(DriverInterface):
    """
    A driver implementation for managing locks using etcd as the backend store.
    
    This driver utilizes the etcd3 client library for interacting with etcd, a distributed key-value store. It
    implements the DriverInterface to provide methods for acquiring and releasing locks.
    """

    def __init__(self, **options):
        """
        Initializes an instance of ETCDDriver.

        Parameters:
            **options: Additional options to be passed to the etcd client.

        Notes:
            This method initializes an instance of ETCDDriver and establishes a connection to the etcd server using
            the provided options.
        """
        self.__connection = client(**options)

    def acquire_lock(self, key) -> None:
        """
        Acquires a lock based on the provided key.

        Parameters:
            key (str): The key used to acquire the lock.

        Raises:
            AcquireLockException: If an error occurs while acquiring the lock.

        Notes:
            This method attempts to acquire a lock by using the etcd client to put a value associated with the key. If
            the key already exists, indicating that the lock is already held, an AcquireLockException is raised.
        """
        if not self.__connection.put_if_not_exists(key, str()):
            raise AcquireLockException()

    def release_lock(self, key) -> None:
        """
        Releases a lock based on the provided key.

        Parameters:
            key (str): The key used to release the lock.

        Raises:
            ReleaseLockException: If an error occurs while releasing the lock.

        Notes:
            This method releases a lock by deleting the key from the etcd server using the etcd client. If the delete
            operation fails, indicating an error in releasing the lock, a ReleaseLockException is raised.
        """
        if not self.__connection.delete(key):
            raise ReleaseLockException()
