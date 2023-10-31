from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
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
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['title', 'vacancy','job_type']
    search_fields = ['title', 'description']
    ordering_fields = ['salary_start','salary_end','experience']
    permission_classes = [IsAuthenticated]
    

class JobDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers