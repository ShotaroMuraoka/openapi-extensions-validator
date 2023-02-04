from __future__ import annotations
from dataclasses import dataclass, field
from .ResponseTemplates import ResponseTemplates
from .ResponseParameters import ResponseParameters

@dataclass
class Response():
    statusCode: str = '200'
    responseTemplates: dict = field(default_factory=list) # https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-responseTemplates.html
    responseParameters: dict = field(default_factory=list)# https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/api-gateway-swagger-extensions-integration-responseParameters.html
    contentHandling: str = ''

    def __post_init__(self) -> None:
        if type(self.responseTemplates) is dict:
            self.responseTemplates = ResponseTemplates(**self.responseTemplates)
        if type(self.responseParameters) is dict:
            self.responseParameters = ResponseParameters(**self.responseParameters)
