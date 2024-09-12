from src.executors.abc_executor import ABCNotificationExecutor
from src.models.notification_enum import SendNotificationStatusEnum
from src.models.notification_models import ExecutionNotificationUnit, SendNotificationStatus


class SMSExecutor(ABCNotificationExecutor):
    def execute(self, notification_unit: ExecutionNotificationUnit, *args, **kwargs) -> SendNotificationStatus:
        print("Executing SMS notification")
        return SendNotificationStatus(
            status=SendNotificationStatusEnum.FAILED,
            recipient=notification_unit.recipient,
            message=notification_unit.message,
            notification_type=notification_unit.notification_type_value,
            error="SMS service is not available",
            created_timestamp_utc=notification_unit.timestamp_utc,
        )
