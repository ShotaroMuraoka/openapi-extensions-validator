from __future__ import annotations
from dataclasses import dataclass, field
from .Response import Response

@dataclass
class Responses():
    responses: dict = field(default_factory=list)

    def __post_init__(self) -> None:
        for response in self.responses:
            Response(response)
