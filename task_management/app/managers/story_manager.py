from functools import lru_cache

from task_management.app.dto.create_payload.story_create_payload import StoryCreatePayloadDTO
from task_management.app.models.story import Story


class StoryManager:

    @lru_cache(maxsize=10)
    def project_manager(self):
        from  task_management.app import project_manager

        return project_manager

    @lru_cache(maxsize=10)
    def task_manager(self):
        from  task_management.app.managers import TaskManager

        return TaskManager()

    def create_story(self, story_payload: StoryCreatePayloadDTO):
        story = Story(story_payload)
        self.project_manager().stories[str(story.id)] = story
        self.tasks_with_story_details(task_ids=story_payload.task_ids , story_id = story_payload.id)
        return story

    def get_story(self, story_id: str) -> Story:
        if not story_id:
            return None
        story = self.project_manager().stories.get(story_id)
        return story

    def remove_task_from_story(self, story_id: str, task_id: str):
        story = self.get_story(story_id)
        # since task are allowed without stories
        if not story:
            print(f'Story not found for given story id {story_id}')
            return

        story.task_ids.remove(task_id)
        return True

    def add_task_into_story(self, story_id, task_id):
        story = self.get_story(story_id)
        # since task are allowed without stories
        if not story:
            print(f'Story not found for given story id {story_id}')
            return

        story.task_ids.append(task_id)
        return True

    def update_story(self, story_id, update_param_name, update_param_value):
        story = self.get_story(story_id)
        # Add validation layer if required
        setattr(story, update_param_name, update_param_value)
        self.update_story_in_store(story_id, story)

    def update_story_in_store(self, story_id, story):
        self.project_manager().stories[story_id] = story


    def tasks_with_story_details(self, task_ids, story_id):
        for task_id in task_ids:
            self.task_manager().update_story_id(task_id, story_id)
        return






