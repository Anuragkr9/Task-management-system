from task_management.app import *

# Input
if __name__ == "__main__":
    task_payload = dict(
        id='task_id1',
        title='task1',
        description='This is about task1',
        deadline='20-03-2024',
        assignees=['user_id1']
    )
    task_payload2 = dict(
        id='task_id2',
        title='task2',
        description='This is about task1',
        deadline='20-03-2024',
        assignees=['user_id2']
    )
    task_payload3 = dict(
        id='task_id3',
        title='task3',
        description='This is about task3',
        deadline='20-03-2024',
        assignees=['user_id3']
    )

    story_payload = dict(
        id='story_id1',
        title='story1',
        description='This is about story1',
        deadline='20-04-2024',
        assignees=['user_id1'],
        type='BUG',
        task_ids=['task_id1', 'task_id2']
    )
    story_payload2 = dict(
        id='story_id2',
        title='story2',
        description='This is about story2',
        deadline='20-04-2024',
        assignees=['user_id2'],
        type='BUG',
        task_ids=['task_id3']
    )
    subtask1_payload = dict(
        id='subtask_id1',
        title='subtask1',
        description='This is about subtask1',
        deadline='20-03-2024',
        assignees=['user_id1'],
        task_id='task_id1'
    )

    task1 = project_manager.create_task(**task_payload)
    task2 = project_manager.create_task(**task_payload2)
    task3 = project_manager.create_task(**task_payload3)
    # task2 = project_manager.delete_task(task_id='task_id1')
    task2 = project_manager.update_task(task_id='task_id1', param_name='status', new_value='IN_PROGRESS')

    story1 = project_manager.create_story(**story_payload)
    story2 = project_manager.create_story(**story_payload2)

    subtask = project_manager.create_subtask(**subtask1_payload)

    project_manager.move_task(task_id='task_id1', new_parent_id='story_id2', task_type='TASK')

    print('----------Tasks--------------')
    for task_id, task in project_manager.tasks.items():
        print(task_id, task.__dict__)

    print('----------STORY--------------')
    for story_id, story in project_manager.stories.items():
        print(story_id, story.__dict__)

    print('----------subtasks--------------')
    for subtask_id, subtask in project_manager.subtasks.items():
        print(subtask_id, subtask.__dict__)

    print("subtasks:", project_manager.subtasks)
    print("users:", project_manager.users)
