from uuid import uuid4

from   task_management.app.dto.create_payload.story_create_payload import StoryCreatePayloadDTO
from   task_management.app.utils.constants import StoryType


class Story:
    def __init__(self, story_payload: StoryCreatePayloadDTO):
        self.id = story_payload.id or uuid4()
        self.status = story_payload.status
        self.title = story_payload.title
        self.description = story_payload.description
        self.priority = story_payload.priority
        self.deadline = story_payload.deadline
        self.priority = story_payload.priority
        self.start_date = story_payload.start_date
        self.end_date = story_payload.end_date
        self.task_ids = story_payload.task_ids or []
        self.type = story_payload.type or StoryType.FEATURE




