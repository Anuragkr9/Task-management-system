from uuid import uuid4

from   task_management.app.dto.create_payload.sub_task_create_payload import SubTaskCreatePayloadDTO

from   task_management.app.utils.constants import TaskSize, TaskStatus, TaskPriority


class SubTask:
    
    def __init__(self, subtask_create_payload: SubTaskCreatePayloadDTO):
        self.id = subtask_create_payload.id or uuid4()
        self.title = subtask_create_payload.title
        self.description = subtask_create_payload.description
        self.deadline = subtask_create_payload.deadline
        self.assignees = subtask_create_payload.assignees
        self.status = subtask_create_payload.status or TaskStatus.NOT_STARTED  # subtask different enum ??
        self.size = subtask_create_payload.size or TaskSize.SMALL
        self.priority = subtask_create_payload.priority or TaskPriority.LOW
        self.started_on = None
        self.completed_on = None
        self.task_id = subtask_create_payload.task_id
