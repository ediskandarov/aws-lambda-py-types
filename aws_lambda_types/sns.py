from typing import Union, Optional, List, Dict

try:
    from typing import TypedDict, Literal
except ImportError:
    from typing_extensions import TypedDict, Literal  # type: ignore


class SNSMessageAttributeDict(TypedDict):
    Type: Literal["Binary", "Number", "String", "String.Array"]
    Value: Union[int, str]


class SNSNotificationDict(TypedDict):
    Message: str
    MessageAttributes: Optional[Dict[str, SNSMessageAttributeDict]]
    MessageId: str
    Signature: str
    SignatureVersion: str
    SigningCertURL: str
    Subject: Optional[str]
    Timestamp: str
    TopicArn: str
    Type: Literal["SubscriptionConfirmation", "Notification", "UnsubscribeConfirmation"]
    UnsubscribeURL: str


class SNSRecordDict(TypedDict):
    EventSource: str
    EventSubscriptionArn: str
    EventVersion: str
    Sns: SNSNotificationDict


class SNSEventDict(TypedDict):
    Records: List[SNSRecordDict]
