from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import JobSerializers
from .models import Job


#@api_view(['GET'])
#def job_list_api(request):
    #jobs = Job.objects.all()
    #data = JobSerializers(jobs,many=True).data
    #return Response({'Jobs':data})


#@api_view(['GET'])
#def job_detail_api(request,id):
    #job = Job.objects.get(id=id)
    #data = JobSerializers(job).data
    #return Response({'Job':data})

#-------------------CBV---------------------



class JobListAPI(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers



class JobDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers