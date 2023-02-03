from __future__ import annotations
from dataclasses import dataclass

@dataclass
class TlsConfig():
    insecureSkipVerification: bool = True

    def __post_init__(self) -> None:
        if type(self.insecureSkipVerification) is not bool:
            raise ValueError('insecureSkipVerification', 'type', 'bool')