from __future__ import annotations
from dataclasses import dataclass, field
from .x_amazon_apigateway_integration import XAmazonApigatewayIntegration


@dataclass
class XAmazonApigatewayIntegrations:
    integrations: list = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.integrations is list:
            for integration in self.integrations:
                XAmazonApigatewayIntegration(**integration)
