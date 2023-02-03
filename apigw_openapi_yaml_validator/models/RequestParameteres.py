from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class RequestParameteres():
    args: dict = field(default_factory=list)

    def __post_init__(self) -> None:
        self.args.pop('property', None)
        for property in self.args.keys():
            if property.startswith('integration.request.') == False:
                raise ValueError(property, 'type', 'integration.request.') # TODO: starts with 'integration.request.'