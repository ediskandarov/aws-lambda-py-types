from typing import Literal, TypedDict, Optional, List, Dict


class SQSAttributesDict(TypedDict):
    ApproximateFirstReceiveTimestamp: int
    ApproximateReceiveCount: int
    MessageDeduplicationId: Optional[int]
    MessageGroupId: Optional[int]
    SenderId: str
    SentTimestamp: int
    SequenceNumber: Optional[int]


class SQSMessageAttributeDict(TypedDict):
    binaryListValues: List[bytes]
    binaryValue: bytes
    dataType: Literal["Binary", "Number", "String"]
    stringListValues: List[str]
    stringValue: str


class SQSRecordDict(TypedDict):
    attributes: SQSAttributesDict
    awsRegion: str
    body: str
    eventSource: str
    eventSourceARN: str
    md5OfBody: str
    messageAttributes: Dict[str, SQSMessageAttributeDict]
    messageId: str
    receiptHandle: str


class SQSEventDict(TypedDict):
    Records: List[SQSRecordDict]
