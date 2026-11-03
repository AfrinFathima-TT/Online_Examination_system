from rest_framework import serializers
from ExaminationApp.models import QuestionDb


class QuestionSerializer(serializers.Serializer):
    question = serializers.CharField(max_length = 200)
    option_a = serializers.CharField(max_length = 100)
    option_b = serializers.CharField(max_length = 100)
    option_c = serializers.CharField(max_length = 100)
    option_d = serializers.CharField(max_length = 100)
    correct_answer = serializers.CharField(max_length = 100)

class SubmissionSerializer(serializers.Serializer):
    student_name = serializers.CharField(max_length=100)
    student_email = serializers.CharField(max_length=200)
    question_id = serializers.IntegerField()
    selected_answer = serializers.CharField(max_length=100)
    submitted_date = serializers.DateTimeField(read_only=True)

    def validate(self,validate_data):
        question_id = validate_data.get("question_id")
        if not QuestionDb.objects.filter(id=question_id).exists():
            raise serializers.ValidationError("Question does not exists....!")
        return validate_data