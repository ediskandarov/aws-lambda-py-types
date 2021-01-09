from typing import TypedDict, Literal, Union, Optional, List, Dict


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
