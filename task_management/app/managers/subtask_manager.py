from functools import lru_cache

from ..dto.create_payload.sub_task_create_payload import SubTaskCreatePayloadDTO
from ..models.subtask import SubTask


class SubTaskManager:

    @lru_cache(maxsize=10)
    def project_manager(self):
        from  task_management.app import project_manager
        return project_manager

    @lru_cache(maxsize=10)
    def task_manager(self):
        from  task_management.app.managers import TaskManager
        return TaskManager()

    def create_subtask(self, subtask_payload: SubTaskCreatePayloadDTO):
        subtask = SubTask(subtask_payload)
        self.project_manager().subtasks[str(subtask.id)] = subtask
        self.task_manager().add_subtask_into_task(task_id=subtask_payload.task_id, subtask_id=str(subtask.id))
        return subtask

    def get_subtask(self, subtask_id):
        return self.project_manager().subtasks.get(subtask_id)

    def remove_subtask_from_task(self, subtask):
        self.task_manager().remove_subtask_from_task(task_id=subtask.task_id, subtask_id=str(subtask.id))
        
    def delete_subtask(self, subtask_id):
        self.remove_subtask_from_task(subtask_id)
        self.delete_subtask_from_store(subtask_id)
        return True
    
    def delete_subtasks(self, subtask_ids):
        for subtask_id in subtask_ids:
            self.delete_subtask_from_store(subtask_id)

    def delete_subtask_from_store(self, subtask_id):
        del self.project_manager().subtasks[subtask_id]

    def update_subtask(self, subtask_id, update_param_name, update_param_value):
        subtask = self.get_subtask(subtask_id)
        # Add validation layer if required
        setattr(subtask, update_param_name, update_param_value)
        self.update_subtask_in_store(subtask_id, subtask)

    def update_subtask_in_store(self, subtask_id, subtask):
        self.project_manager().subtasks[subtask_id] = subtask

    def move_subtask(self, subtask_id, task_id):
        subtask = self.get_subtask(subtask_id)
        if not subtask:
            print('subtask not found')
            return False
        self.remove_subtask_from_task(subtask)
        subtask.task_id = task_id
        self.update_subtask_in_store(subtask_id, subtask)

