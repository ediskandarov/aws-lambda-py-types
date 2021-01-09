from typing import TypedDict, Literal, Union, Optional, List, Dict


class SNSMessageAttributeDict(TypedDict):
    Type: Literal["String", "String.Array", "Number", "Binary"]
    Value: Union[int, str]


class SNSNotificationDict(TypedDict):
    Type: Literal["Notification", "UnsubscribeConfirmation", "SubscriptionConfirmation"]
    MessageId: str
    Message: str
    Subject: Optional[str]
    Timestamp: str
    TopicArn: str
    SignatureVersion: str
    Signature: str
    SigningCertURL: str
    UnsubscribeURL: str
    MessageAttributes: Optional[Dict[str, SNSMessageAttributeDict]]


class SNSRecordDict(TypedDict):
    EventSource: str
    EventVersion: str
    EventSubscriptionArn: str
    Sns: SNSNotificationDict


class SNSEventDict(TypedDict):
    Records: List[SNSRecordDict]
