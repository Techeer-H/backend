from rest_framework import serializers
from .models import *
from feedback.models import Feedback

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = '__all__'

class StudentRegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ["id", "academy_id", "name", "birth", "phone", "school", "grade", "parent_name", "parent_phone"]

class ScoreSerializer(serializers.ModelSerializer):
  class Meta:
    model = StudentScore
    fields = '__all__'

class ScoretRegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = StudentScore
    fields = ["id", "subject_id", "exam_id", "type", "score", "grade"]