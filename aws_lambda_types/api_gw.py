from typing import Dict, List, Literal, Optional, TypedDict
from .http import HTTP_METHODS


class APIGWPayloadV1RequestContextIdentityDict(TypedDict):
    accessKey: Optional[str]
    accountId: Optional[str]
    caller: Optional[str]
    cognitoAmr: Optional[str]
    cognitoAuthenticationProvider: Optional[str]
    cognitoAuthenticationType: Optional[str]
    cognitoIdentityId: Optional[str]
    cognitoIdentityPoolId: Optional[str]
    principalOrgId: Optional[str]
    sourceIp: Optional[str]
    user: Optional[str]
    userAgent: Optional[str]
    userArn: Optional[str]


class APIGWPayloadV1RequestContextDict(TypedDict):
    accountId: str
    apiId: str
    domainName: str
    domainPrefix: str
    extendedRequestId: str
    httpMethod: HTTP_METHODS
    identity: APIGWPayloadV1RequestContextIdentityDict
    path: str
    protocol: str
    requestId: str
    requestTime: str
    requestTimeEpoch: int
    resourceId: str
    resourcePath: str
    stage: str


class APIGWPayloadV1RequestDict(TypedDict):
    body: str
    headers: Dict[str, str]
    httpMethod: str
    isBase64Encoded: bool
    multiValueHeaders: Dict[str, List[str]]
    multiValueQueryStringParameters: Dict[str, List[str]]
    path: str
    pathParameters: Optional[Dict[str, str]]
    queryStringParameters: Dict[str, str]
    requestContext: APIGWPayloadV1RequestContextDict
    resource: str
    stageVariables: Optional[Dict[str, str]]
    version: Literal["1.0"]


class APIGWPayloadV1ResponseDict(TypedDict):
    isBase64Encoded: bool
    statusCode: int
    headers: Dict[str, str]
    multiValueHeaders: Dict[str, List[str]]
    body: str
