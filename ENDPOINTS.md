# Overview
The API revolves around Assignments, Submissions and Grades endpoints. In addition to those, we also rely on Users and Groups endpoints.
There is no Homework object per se. Rather, its composed of multiple objects.

### /users
- Methods: get, post, patch, delete (may not be available for all users)
- Permissions: Authenticated. Staff can do anything. Read only for Students
- Description: mainly there so Staff can manage all users. Students can only view/edit themselves.

### /groups
- Methods: get, post, patch, delete (may not be available for all users)
- Permissions: Authenticated. Only for Staff.
- Description: Only for staff members so they can manage student membership in classes.

### /assignments
- Methods: get, post, patch, delete (may not be available for all users)
- Permissions: Authenticated.  Staff can do anything. Read only for Students.
- Description: Staff can create assignments. Students can view assignments.
- filters: {'name': ['exact'], 'submissions': ['isnull'], 'submissions__grade': ['isnull']}

### /submissions
- Methods: get, post, patch, delete (may not be available for all users)
- Permissions: Authenticated.  Is owner or staff. Students can create and edit only their own submissions.
- Description: Students create their submission for a given assignment.
- filters: {'grade': ['exact', 'isnull'], 'grade__final_grade': ['exact'], 'assignment__name': ['exact'],
                     'created': ['gte', 'lte', 'exact']}
                     
### /grades
- Methods: get, post, patch, delete (may not be available for all users)
- Permissions: Authenticated. Staff can do anything. Read only for Students.
- Description: Staff can create grades for a given submission. Students only view their own grades.
- filters: ('final_grade', 'submission__assignment__name', )     