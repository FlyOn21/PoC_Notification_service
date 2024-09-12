from typing import Union, Mapping, Optional

from pydantic import BaseModel, Field

from datetime import datetime

from src.models.notification_enum import Recipients, NotificationType, SendNotificationStatusEnum


class InputNotificationUnit(BaseModel):
    recipients: Mapping[Recipients, NotificationType] = Field(
        title="Mapping Recipients: NotificationType", description="Mapping of recipients to notification types"
    )
    message: Union[str, dict] = Field(title="Message", description="The message to be sent")


class ExecutionNotificationUnit(BaseModel):
    recipient: Recipients = Field(title="Recipient", description="The recipient of the notification")
    notification_type_value: str = Field(title="Notification type value", description="The type of notification")
    message: Union[str, dict] = Field(title="Message", description="The message to be sent")
    timestamp_utc: int = Field(
        title="Timestamp",
        description="The timestamp of the notification",
        default_factory=lambda: int(datetime.utcnow().timestamp()),
    )


class SendNotificationStatus(BaseModel):
    status: SendNotificationStatusEnum = Field(title="Status", description="The status of the notification")
    recipient: Recipients = Field(title="Recipient", description="The recipient of the notification")
    notification_type: str = Field(title="Notification Type", description="The type of notification")
    created_timestamp_utc: int = Field(
        title="Created Timestamp",
        description="The timestamp of the notification creation",
    )
    message: Union[str, dict] = Field(title="Message", description="The message that failed to send")
    error: Optional[str] = Field(title="Error", description="The error massage", default_factory=lambda: None)
