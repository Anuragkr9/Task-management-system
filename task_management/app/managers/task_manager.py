from functools import lru_cache


from  task_management.app import project_manager
from ..dto.create_payload.task_create_payload import TaskCreatePayloadDTO
from ..models.task import Task


class TaskManager:

    @lru_cache(maxsize=10)
    def story_manager(self):
        from .story_manager import StoryManager
        return StoryManager()

    @lru_cache(maxsize=10)
    def subtask_manager(self):
        from .subtask_manager import SubTaskManager

        return SubTaskManager()

    def create_task(self, task_payload: TaskCreatePayloadDTO):
        task = Task(task_payload)
        project_manager.tasks[str(task.id)] = task
        if task_payload.story_id:
            self.story_manager().add_task_into_story(story_id=task_payload.story_id, task_id=str(task.id))

        return task


    def get_task(self, task_id):
        return project_manager.tasks.get(task_id)

    def add_subtask_into_task(self, task_id, subtask_id):
        task = self.get_task(task_id)

        if not task:
            print('Task not found')
            return

        task.subtask_ids.append(subtask_id)
        return

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        self.remove_task_from_current_story(task)
        self.subtask_manager().delete_subtasks(task.subtask_ids)
        self.delete_from_store(task_id)
        return True


    # This function will be used to update desc, title, assignes or any other params
    def update_task(self, task_id, update_param_name, update_param_value):
        task = self.get_task(task_id)
        if not task:
            print('Task not found')
            return

        # Add validation layer if required
        setattr(task, update_param_name, update_param_value)
        self.update_task_in_store(task_id, task)

    def update_task_in_store(self, task_id, task):
        project_manager.tasks[task_id] = task

    def remove_subtask_from_task(self, task_id, subtask_id):
        pass

    def delete_from_store(self, task_id):
        del project_manager.tasks[task_id]

    def remove_task_from_current_story(self, task):
        self.story_manager().remove_task_from_story(story_id=task.story_id, task_id=str(task.id))

    def move_task(self, task_id, story_id):
        task = self.get_task(task_id)
        if not task:
            print('Task not found')
            return False
        self.remove_task_from_current_story(task)
        task.story_id = story_id
        self.story_manager().add_task_into_story(story_id, task_id)
        self.update_task_in_store(task_id, task)

    def filter_tasks_by_user_id(self, user_id):
        tasks = project_manager.tasks
        user_tasks = []
        for task in tasks:
            if user_id in task.assignees:
                user_tasks.append(task)

        return user_tasks

    def get_task_by_user(self, user_id):
        user_tasks = self.filter_tasks_by_user_id(user_id)
        return user_tasks

    def update_story_id(self, task_id, story_id):
        task = self.get_task(task_id)
        if not task:
            print('Task not found')
            return

        task.story_id = story_id
        return

    def add_task_in_new_story(self, task, story_id):
        self.story_manager().update_tasks_with_story_details(task_ids=[str(task.id)], story_id=story_id)





