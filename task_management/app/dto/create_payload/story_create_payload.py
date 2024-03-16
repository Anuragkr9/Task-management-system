from dataclasses import dataclass
from typing import List

from   task_management.app.dto.create_payload.base_create_payload import BasePayloadDTO


@dataclass
class StoryCreatePayloadDTO(BasePayloadDTO):
    status: str  # add valid choices
    priority: str  # add valid choices
    start_date: str
    end_date: str
    task_ids: List
    type: str
    deadline: int = None
