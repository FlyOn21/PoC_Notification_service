import asyncio
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from typing import List

from src.models.notification_enum import SendNotificationStatusEnum
from src.models.notification_models import InputNotificationUnit, ExecutionNotificationUnit, SendNotificationStatus
from src.executors.kafka_executor import KafkaExecutor
from src.executors.rabbit_mq_executor import RabbitMQExecutor
from src.executors.sms_executor import SMSExecutor


class NotificationController:
    """
    Controller class for managing and sending notifications using different executors.
    """

    def __init__(self):
        """
        Initialize the NotificationController with available notification types and their corresponding executors.
        """
        self.__notification_types = {
            "sms": SMSExecutor(),
            "kafka": KafkaExecutor(),
            "rabbit_mq": RabbitMQExecutor(),
        }

    async def send_notification(self, input_notification_units: List[InputNotificationUnit]) -> None:
        """
        Send notifications asynchronously using the appropriate executors.

        Args:
            input_notification_units (List[InputNotificationUnit]): List of input notification units to be processed.
        """
        loop = asyncio.get_event_loop()
        with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as pool:
            for input_notification_unit in input_notification_units:
                msg = input_notification_unit.message
                loop_result = await asyncio.gather(
                    *[
                        loop.run_in_executor(
                            pool,
                            self.__notification_types[notif_type.value].execute,
                            ExecutionNotificationUnit(
                                recipient=recipient,
                                notification_type_value=notif_type.value,
                                message=msg,
                            ),
                        )
                        for recipient, notif_type in input_notification_unit.recipients.items()
                    ]
                )
                for send_notification_status in loop_result:
                    if send_notification_status.status == SendNotificationStatusEnum.FAILED:
                        await self.__logging_notification_failed(send_notification_status)
                    else:
                        await self.__logging_notification_success(send_notification_status)
        return

    async def __logging_notification_failed(self, send_notification_status: SendNotificationStatus) -> None:
        log_message = (
            f"\nFailed to send notification:\n"
            f"Recipient: {send_notification_status.recipient.value}\n"
            f"Notification Type: {send_notification_status.notification_type}\n"
            f"Message: {send_notification_status.message}\n"
            f"Error: {send_notification_status.error}\n"
            f"Created At: {send_notification_status.created_timestamp_utc}\n"
            f"Status: {send_notification_status.status.value}\n"
        )
        print(log_message)

    async def __logging_notification_success(self, send_notification_status: SendNotificationStatus) -> None:
        log_message = (
            f"\nNotification sent successfully:\n"
            f"Recipient: {send_notification_status.recipient.value}\n"
            f"Notification Type: {send_notification_status.notification_type}\n"
            f"Message: {send_notification_status.message}\n"
            f"Status: {send_notification_status.status.value}\n"
            f"Created At: {send_notification_status.created_timestamp_utc}\n"
        )
        print(log_message)
