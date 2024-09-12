from enum import Enum


class NotificationType(Enum):
    SMS = "sms"
    KAFKA = "kafka"
    RABBIT_MQ = "rabbit_mq"


class Recipients(str, Enum):
    PRODUCTS_SERVICE = "products_service"
    ODOO_SERVICE = "odoo_service"
    CUSTOMER_SERVICE = "customer_service"


class SendNotificationStatusEnum(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"
