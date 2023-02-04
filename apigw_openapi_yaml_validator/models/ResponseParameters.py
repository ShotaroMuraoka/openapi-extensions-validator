from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class ResponseParameters():
    args: dict = field(default_factory=list)

    def __post_init__(self) -> None:
        self.args.pop('property', None)
        for property in self.args.keys():
            if property.startswith('method.response.header.') == False:
                raise ValueError(property, 'type', 'method.response.header.') # TODO: starts with 'integration.request.'