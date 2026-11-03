from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from ExaminationApp.models import QuestionDb,Submissionsdb
from ExaminationApp.serializers import QuestionSerializer,SubmissionSerializer

# Create your views here.
class QuestionListCreateView(APIView):
    def get(self,request):
        qs = QuestionDb.objects.all()
        seriallizer_instance = QuestionSerializer(qs,many=True)  

        return Response(data=seriallizer_instance.data)
    def post(self,request):
        form_data = request.data  

        serializer_instance = QuestionSerializer(data=form_data)

        if  serializer_instance.is_valid():

            actual_data = serializer_instance.validated_data

            
            QuestionDb.objects.create(**actual_data)

            return Response(data={"message" : "Question added successfully"})
        else:
            return Response(data={"errors" : serializer_instance.errors})


class QuestionRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):

        qs = QuestionDb.objects.get(id = pk)

        serializer_instance = QuestionSerializer(qs)

        return Response(data = serializer_instance.data)

    def put(self,request,pk):
        form_data = request.data     #get data from client

        serializer_instance = QuestionSerializer(data = form_data)
        if serializer_instance.is_valid():

            actual_data = serializer_instance.validated_data

            QuestionDb.objects.filter(id = pk).update(**actual_data)

            return Response(data=serializer_instance.data)
        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):

        QuestionDb.objects.filter(id = pk).delete()

        return Response({
                "Message" : "Question deleted successfully...!"
        })

class SubmissionsListCreateView(APIView):
    def get(self,request):
        qs = Submissionsdb.objects.all()
        submission_instance = SubmissionSerializer(qs,many=True)
        return Response(data=submission_instance.data)

    def post(self,request):
        forrm_data = request.data
        submission_instance = SubmissionSerializer(data = forrm_data)
        if submission_instance.is_valid():
            actual_data = submission_instance.validated_data

            Submissionsdb.objects.create(**actual_data)
            return Response(data={"Message" : "Answer added successfully...!"})
        else:
            return Response(data={"errors":submission_instance.errors})



class SubmissionsRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):

        qs = get_object_or_404(Submissionsdb,id=pk)
        serializer_instance = SubmissionSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):

        form_data = request.data
        serializer_instance = SubmissionSerializer(data = form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            Submissionsdb.objects.filter(id = pk).update(**actual_data)
            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        Submissionsdb.objects.filter(id = pk).delete()

        return Response({"Message" : "Answer deleted successfully"})