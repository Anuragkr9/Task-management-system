from functools import lru_cache

from   task_management.app.dto.create_payload.story_create_payload import StoryCreatePayloadDTO
from   task_management.app.dto.create_payload.sub_task_create_payload import SubTaskCreatePayloadDTO
from   task_management.app.dto.create_payload.task_create_payload import TaskCreatePayloadDTO
from   task_management.app.utils.constants import TaskType


class ProjectManager:

    def __init__(self):
        self.users = dict()
        self.stories = dict()
        self.tasks = dict()
        self.subtasks = dict()

    @lru_cache(maxsize=10)
    def task_manager(self):
        from   task_management.app.managers.task_manager import TaskManager

        return TaskManager()

    @lru_cache(maxsize=10)
    def story_manager(self):
        from   task_management.app.managers.story_manager import StoryManager

        return StoryManager()

    @lru_cache(maxsize=10)
    def subtask_manager(self):
        from   task_management.app.managers.subtask_manager import SubTaskManager

        return SubTaskManager()

    def move_task(self, task_id, new_parent_id, task_type):
        if task_type == TaskType.SUBTASK:
            self.subtask_manager().move_subtask(subtask_id=task_id, task_id=new_parent_id)
        if task_type == TaskType.TASK:
            self.task_manager().move_task(task_id=task_id, story_id=new_parent_id)

    def create_task(self, **kwargs):
        task_payload = self.create_task_payload(**kwargs)
        return self.task_manager().create_task(task_payload)

    def create_task_payload(self, **kwargs):
        return TaskCreatePayloadDTO(
            id = kwargs.get('id'),
            title=kwargs.get('title'),
            description=kwargs.get('description'),
            status=kwargs.get('status'),
            assignees=kwargs.get('assignees'),
            size=kwargs.get('size'),
            deadline=kwargs.get('deadline'),
            priority=kwargs.get('priority'),
            story_id=kwargs.get('story_id'),
            end_date=kwargs.get('end_date'),
            start_date=kwargs.get('start_date')
        )

    def create_story(self, **kwargs):
        story_payload = self.create_story_payload(**kwargs)
        self.story_manager().create_story(story_payload)

    def create_story_payload(self, **kwargs):
        return StoryCreatePayloadDTO(
            id=kwargs.get('id'),
            title=kwargs.get('title'),
            description=kwargs.get('description'),
            status=kwargs.get('status'),
            priority=kwargs.get('priority'),
            start_date=kwargs.get('start_date'),
            end_date=kwargs.get('end_date'),
            task_ids=kwargs.get('task_ids'),
            type=kwargs.get('type'),
            deadline=kwargs.get('deadline'),
        )

    def create_subtask(self, **kwargs):
        subtask_payload = self.create_subtask_payload(**kwargs)
        self.subtask_manager().create_subtask(subtask_payload)

    def create_subtask_payload(self, **kwargs):
        return SubTaskCreatePayloadDTO(
            id=kwargs.get('id'),
            title=kwargs.get('title'),
            description=kwargs.get('description'),
            status=kwargs.get('status'),
            assignees=kwargs.get('assignees'),
            size=kwargs.get('size'),
            deadline=kwargs.get('deadline'),
            priority=kwargs.get('priority'),
            end_date=kwargs.get('end_date'),
            start_date=kwargs.get('start_date'),
            task_id=kwargs.get('task_id')
        )


    def create_user(self, **kwargs):
        pass

    def get_user_workload(self, user_id):
        self.task_manager().get_task_by_user(user_id)

    def delete_task(self, task_id):
        self.task_manager().delete_task(task_id=task_id)

    def update_task(self, task_id, param_name, new_value):
        task = self.task_manager().update_task(task_id, update_param_name=param_name, update_param_value=new_value)
        return task



project_manager = ProjectManager()
