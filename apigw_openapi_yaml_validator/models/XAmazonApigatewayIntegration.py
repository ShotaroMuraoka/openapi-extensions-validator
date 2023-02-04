from __future__ import annotations
from dataclasses import dataclass, field
from .RequestParameters import RequestParameters
from .RequestTemplates import RequestTemplates
from .Responses import Responses
from .TlsConfig import TlsConfig

@dataclass
class  XAmazonApigatewayIntegration():
    cacheKeyParameters: list = field(default_factory=list)
    cacheNamespace: str = ''
    connectionId: str = ''
    connectionType: str = 'INTERNET'
    credentials: str = ''
    contentHandling: str = 'CONVERT_TO_BINARY'
    httpMethod: str = ''
    integrationSubtype: str = ''
    passthroughBehavior: str = '' # TODO: https://docs.aws.amazon.com/ja_jp/apigateway/latest/api/API_Integration.html#passthroughBehavior
    payloadFormatVersion: str = ''
    requestParameters: dict = field(default_factory=list) # https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-requestParameters.html
    requestTemplates: dict = field(default_factory=list) # https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-requestTemplates.html
    responses: dict = field(default_factory=list) # https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-responses.html
    timeoutInMillis: int = 0
    type: str = 'HTTP'
    tlsConfig: dict = field(default_factory=list) # https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/api-gateway-extensions-integration-tls-config.html
    uri: str = ''

    def __post_init__(self) -> None:
        # TODO: 
        if type(self.requestParameters) is dict:
            self.requestParameters = RequestParameters(self.requestParameters)
        if type(self.requestTemplates) is dict:
            self.requestTemplates = RequestTemplates(self.requestTemplates)
        if type(self.responses) is dict:
            self.responses = Responses(**self.responses)
        if type(self.tlsConfig) is dict:
            self.tlsConfig = TlsConfig(**self.tlsConfig)
        if type(self.cacheKeyParameters) is not list:
            raise ValueError('cacheKeyParameters', 'type', 'array')
        if type(self.timeoutInMillis) is not int:
            raise ValueError('timeoutInMillis', 'type', 'int')
        if self.type.upper() not in ['HTTP', 'AWS', 'MOCK', 'HTTP_PROXY', 'AWS_PROXY']:
            raise ValueError('type', 'value', 'HTTP|VPC_LINK|AWS|MOCK|HTTP_PROXY|AWS_PROXY')
        if self.connectionType.upper() not in ['INTERNET', 'VPC_LINK']:
            raise ValueError('connectionType', 'value', 'INTERNET|VPC_LINK')
        if self.contentHandling.upper() not in ['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']:
            raise ValueError('contentHandling', 'value', 'CONVERT_TO_BINARY|CONVERT_TO_TEXT')

    def validated() -> list:
        return []