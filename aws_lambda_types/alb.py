from typing import Dict, List

from typing_extensions import TypedDict

from .http import HTTP_METHODS


class ALBRequestContextELBDict(TypedDict):
    targetGroupArn: str


class ALBRequestContextDict(TypedDict):
    elb: ALBRequestContextELBDict


class ALBRequestDict(TypedDict):
    body: str
    headers: Dict[str, str]
    httpMethod: HTTP_METHODS
    isBase64Encoded: bool
    path: str
    queryStringParameters: Dict[str, str]
    requestContext: ALBRequestContextDict


class ALBResponseDict(TypedDict):
    isBase64Encoded: bool
    statusCode: int
    statusDescription: str
    headers: Dict[str, str]
    body: str


class ALBMultiValueRequestDict(TypedDict):
    body: str
    httpMethod: HTTP_METHODS
    isBase64Encoded: bool
    multiValueHeaders: Dict[str, List[str]]
    multiValueQueryStringParameters: Dict[str, List[str]]
    path: str
    requestContext: ALBRequestContextDict


class ALBMultiValueResponseDict(TypedDict):
    isBase64Encoded: bool
    statusCode: int
    statusDescription: str
    multiValueHeaders: Dict[str, List[str]]
    body: str
