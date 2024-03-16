from uuid import uuid4
import datetime

from  task_management.app.dto.create_payload.task_create_payload import TaskCreatePayloadDTO
from   task_management.app.utils.constants import TaskSize, TaskStatus, TaskPriority


class Task:
    def __init__(self, task_payload: TaskCreatePayloadDTO):
        self.id = task_payload.id or uuid4()
        self.title = task_payload.title
        self.description = task_payload.description
        self.deadline = task_payload.deadline
        self.assignees = task_payload.assignees
        self.status = task_payload.status or TaskStatus.NOT_STARTED
        self.size = task_payload.size or TaskSize.SMALL
        self.priority = task_payload.priority or TaskPriority.LOW
        self.start_date = task_payload.start_date
        self.end_date = task_payload.end_date
        self.story_id = task_payload.story_id
        self.subtask_ids = []
