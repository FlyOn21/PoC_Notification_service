from abc import ABC, abstractmethod

from src.models.notification_models import ExecutionNotificationUnit, SendNotificationStatus


class ABCNotificationExecutor(ABC):
    """
    Abstract base class for notification executors.

    This class defines the interface for executing notifications.
    Subclasses must implement the `execute` method.
    """

    @abstractmethod
    def execute(self, notification_unit: ExecutionNotificationUnit, *args, **kwargs) -> SendNotificationStatus:
        """
        Execute the notification.

        Args:
            notification_unit (ExecutionNotificationUnit): The notification unit to be executed.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            SendNotificationStatus: The status of the notification send operation.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError
