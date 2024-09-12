from src.executors.abc_executor import ABCNotificationExecutor
from src.models.notification_enum import SendNotificationStatusEnum
from src.models.notification_models import ExecutionNotificationUnit, SendNotificationStatus


class KafkaExecutor(ABCNotificationExecutor):
    def execute(self, notification_unit: ExecutionNotificationUnit, *args, **kwargs) -> SendNotificationStatus:
        print("Executing Kafka notification")
        return SendNotificationStatus(
            status=SendNotificationStatusEnum.SUCCESS,
            notification_type=notification_unit.notification_type_value,
            recipient=notification_unit.recipient,
            created_timestamp_utc=notification_unit.timestamp_utc,
            message=notification_unit.message,
        )
