# aws-lambda-py-types

[![Test](https://github.com/emcpow2/aws-lambda-py-types/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/emcpow2/aws-lambda-py-types/actions/workflows/main.yml)

Type definitions for AWS Lambda events using Python type hinting.

## A Simple Example

```py
from aws_lambda_types.sns import SNSEventDict


def lambda_handler(event: SNSEventDict, context):
    message = event["Records"][0]["Sns"]["Message"]
    print("From SNS: " + message)
    return message
```

![usage.gif](https://raw.githubusercontent.com/emcpow2/aws-lambda-py-types/main/docs/usage.gif)

## Useful documentation

- [Application Load Balancers - Lambda functions as targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html)
- [Using AWS Lambda with Amazon SNS](https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html)
- [Working with AWS Lambda proxy integrations for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html)
