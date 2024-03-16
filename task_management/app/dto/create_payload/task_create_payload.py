from dataclasses import dataclass
from typing import List

from   task_management.app.dto.create_payload.base_create_payload import BasePayloadDTO


@dataclass()
class TaskCreatePayloadDTO(BasePayloadDTO):
    status: str  # add valid choices
    priority: str  # add valid choices
    assignees: List
    size: str  # add valid choices
    start_date: str
    end_date: str
    story_id: str = None
    deadline: int = None
