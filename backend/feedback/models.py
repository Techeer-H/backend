from django.db import models
from student.models import Student
from user.models import User

# Create your models here.
class Feedback(models.Model):
	id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(User, related_name="user_feedback", on_delete=models.CASCADE, null=False, db_column="user_id")
	student_id = models.ForeignKey(Student, related_name="student_feedback", on_delete=models.CASCADE, null=False, db_column="student_id")
	student_rating = models.BigIntegerField(null=False)
	parent_rating = models.BigIntegerField(null=True)
	content = models.TextField(max_length=500, null=False, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=False)
	updated_at = models.DateTimeField(auto_now=True, null=True)
