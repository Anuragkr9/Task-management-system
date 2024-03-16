from dataclasses import dataclass
from typing import Optional


@dataclass
class BasePayloadDTO:
    id: Optional[str]
    title: str
    description: str


