from kazoo.client import KazooClient
from driver_exceptions import AcquireLockException, ReleaseLockException
from driver_interface import DriverInterface


class ZookeeperDriver(DriverInterface):
    """
    A driver implementation for managing locks using ZooKeeper as the backend store.

    This driver utilizes the Kazoo client library for interacting with ZooKeeper, a distributed coordination service. It
    implements the DriverInterface to provide methods for acquiring and releasing locks.
    """

    def __init__(self, **options):
        """
        Initializes an instance of ZookeeperDriver.

        Parameters:
            **options: Additional options to be passed to the KazooClient.

        Notes:
            This method initializes an instance of ZookeeperDriver and establishes a connection to the ZooKeeper
            ensemble using the provided options.
        """
        self.__connection = KazooClient(**options)
        self.__connection.start()

    def acquire_lock(self, key):
        """
        Acquires a lock based on the provided key.

        Parameters:
            key (str): The key used to acquire the lock.

        Raises:
            AcquireLockException: If an error occurs while acquiring the lock.

        Notes:
            This method attempts to acquire a lock by creating a znode in ZooKeeper using the Kazoo client. If the
            creation of the znode fails, indicating that the lock is already held or an error occurred, an
            AcquireLockException is raised.
        """
        if not self.__connection.create(key):
            raise AcquireLockException()

    def release_lock(self, key):
        """
        Releases a lock based on the provided key.

        Parameters:
            key (str): The key used to release the lock.

        Raises:
            ReleaseLockException: If an error occurs while releasing the lock.

        Notes:
            This method releases a lock by deleting the znode associated with the key from ZooKeeper using the Kazoo
            client. If the delete operation fails, indicating an error in releasing the lock, a ReleaseLockException is
            raised.
        """
        if not self.__connection.delete(key):
            raise ReleaseLockException()
