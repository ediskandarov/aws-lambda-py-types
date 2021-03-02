import pytest
from pydantic import ValidationError

from aws_lambda_types import alb, api_gw, event_bridge, sns, sqs


@pytest.mark.parametrize(
    "sample_json,pydantic_model",
    [
        ("alb.json", alb.ALBRequestDict),
        ("alb-response.json", alb.ALBResponseDict),
        ("alb-with-multivalue.json", alb.ALBMultiValueRequestDict),
        ("alb-with-multivalue-response.json", alb.ALBMultiValueResponseDict),
        ("api-gateway-payload-v1.json", api_gw.APIGWPayloadV1RequestDict),
        ("api-gateway-payload-v1-response.json", api_gw.APIGWPayloadV1ResponseDict),
        ("api-gateway-payload-v2.json", api_gw.APIGWPayloadV2RequestDict),
        ("api-gateway-payload-v2-response.json", api_gw.APIGWPayloadV2ResponseDict),
        ("cloudwatch.json", event_bridge.ScheduledEventDict),
        ("sns-to-sqs-raw-message-delivery.json", sqs.SQSEventDict),
        ("sns-to-sqs.json", sqs.SQSEventDict),
        ("sqs.json", sqs.SQSEventDict),
        ("sns.json", sns.SNSEventDict),
    ],
    indirect=True,
)
def test_alb_response_dict_validation(sample_json, pydantic_model):
    pydantic_model.parse_obj(sample_json)

    invalid_alb_response = sample_json.copy()
    # Set an invalid object to test validation error trigger
    invalid_alb_response["body"] = lambda x: x
    with pytest.raises(ValidationError):
        pydantic_model.parse_obj(invalid_alb_response)
