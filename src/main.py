import asyncio

from src.models.notification_enum import Recipients, NotificationType
from src.models.notification_models import InputNotificationUnit
from src.services.notification_controller import NotificationController


async def main():
    test = [
        InputNotificationUnit(
            recipients={
                Recipients.ODOO_SERVICE: NotificationType.SMS,
                Recipients.CUSTOMER_SERVICE: NotificationType.KAFKA,
            },
            message="Test message",
        ),
        InputNotificationUnit(
            recipients={
                Recipients.PRODUCTS_SERVICE: NotificationType.RABBIT_MQ,
            },
            message="Test message 2",
        ),
    ]
    notification_controller = NotificationController()
    await notification_controller.send_notification(test)


if __name__ == "__main__":
    asyncio.run(main())
