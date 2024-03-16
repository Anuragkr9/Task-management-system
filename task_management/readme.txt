task_management system
classes required
    - Storey
    - task
    - subtask
    - user

Manager
    - TaskManager
    - Storeymanager
    - subtaskManager
    - UserManager


EnumClass
    - priority
    - status
    - type


    - task = {
        task_id1: task1(object of task class)
        task_id2: task2
        task_id3: task3
    }

design Pattern
    - factory
    - strategy pattern for move operation
task and subtask create factory???



project
    - id
    - stories: [storey_id]
    - title
    - description
    - start_date
    - end_date

story
    - id
    - tasks
    - title
    - description
    - type
    - start_date
    - end_date
    - status
    - priority

    #extension
    - team_members
    - project_id




Task
    - id
    - title
    - description
    - deadline
    - status
    - started_on
    - completed_on
    - priority
    - Assignees
    - created_by
    - storey_id
    - subtasks : List[subtask]


subtask
        - id
        - parent_task_id
        - title
        - deadline
        - started_on
        - completed_on
        - priority
        - assignees


user
    - id
    - name
    - dept
    - email
    - team
    - status

  prop:
    - is_logged_in
    - is_active

  methods:
    - login
    - logout
    - view_tasks


Admin user
  register_user(user_details)
    -


Move (task_id, new_parent_id)
    - handle dependencies
    - task -> storey
    - subtask -> task


FR:
    - create user
    - login/logout of user
    - CRUD of task/subtask/storey
    - Move task
    - Get workload of the user


Assumptions:
    -
    - can a task be independent i.e without being part of any storey? YES
    - moving one task from one storey to another storey will that affect
     the start and end date of the corresponding stories? No (Ideally Yes, we can if time permits)
        - In case of yes, we need to handle days_allotted, start_end, end_date and others attributes
        - We can handle it using update deadline functionality

    - deleting a task will delete all its subtasks? YES
        - Do we need to adjust timeline? same as above
    -
NFR:
    - Authorization of task/storey?
    - Authorization can be added on any storey or task update action
    -


To be visited:
    - factory for task and substask?

