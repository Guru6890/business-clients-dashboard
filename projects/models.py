from django.db import models

import uuid

# Create your models here.

class Project(models.Model):
    class STATUS(models.TextChoices):
        PLANNING = 'planning', 'Planning'
        IN_PROGRESS = 'in_progress', 'In Progress'
        REVIEW = 'review', 'Review'
        COMPLETED = 'completed', 'Completed'
        ARCHIVED = 'archived', 'Archived'

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    company = models.ForeignKey('clients.Company', on_delete=models.RESTRICT, related_name='projects', db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=11, choices=STATUS.choices, default=STATUS.PLANNING, db_index=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True, null=True)

class Task(models.Model):
    class STATUS(models.TextChoices):
        TODO = 'todo', 'To do'
        IN_PROGRESS = 'in_progress', 'In Progress'
        DONE = 'done', 'Done'
        BLOCKED = 'blocked', 'Blocked'

    class PRIORITY(models.TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'
        CRITICAL = 'critical', 'Critical'

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=11, choices=STATUS.choices, default=STATUS.TODO)
    priority = models.CharField(max_length=8, choices=PRIORITY.choices, default=PRIORITY.MEDIUM)
    asigned_to = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='tasks')
    due_date = models.DateField(blank=True)