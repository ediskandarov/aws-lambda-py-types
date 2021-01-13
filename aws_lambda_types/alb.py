from typing import Dict, List, TypedDict


class ALBRequestContextELBDict(TypedDict):
    targetGroupArn: str


class ALBRequestContextDict(TypedDict):
    elb: ALBRequestContextELBDict


class ALBRequestDict(TypedDict):
    body: str
    headers: Dict[str, str]
    httpMethod: str
    isBase64Encoded: bool
    path: str
    queryStringParameters: Dict[str, str]
    requestContext: ALBRequestContextDict


class ALBMultiValueRequestDict(TypedDict):
    body: str
    httpMethod: str
    isBase64Encoded: bool
    multiValueHeaders: Dict[str, List[str]]
    multiValueQueryStringParameters: Dict[str, List[str]]
    path: str
    requestContext: ALBRequestContextDict
