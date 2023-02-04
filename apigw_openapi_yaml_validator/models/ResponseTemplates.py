from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class ResponseTemplates():
    args: dict = field(default_factory=list)

    def __post_init__(self) -> None:
        #  FIXME: to validate mime-types
        pass