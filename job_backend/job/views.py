from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status, authentication, permissions

from .forms import JobForm

from .models import Job , Category

from .serializers import *

class NewestJobsView(APIView):
    def get(self, request, format=None):
        jobs= Job.objects.all()[0:4]
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    
class JobsDetailView(APIView):
    def get(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        serializer = JobDetailSerializer(job)
        return Response(serializer.data)

class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class BrowseJobsView(APIView):
    def get(self, request, format=None):
        jobs= Job.objects.all()
        categories = request.GET.get('categories', '')
        query = request.GET.get('query', '')

        if query:
            jobs = jobs.filter(title__icontains=query)

        if categories:
            jobs = jobs.filter(category_id__in = categories.split(','))



        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)


class MyJobsView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        myjobs = Job.objects.filter(created_by = request.user)

        serializer = JobSerializer(myjobs, many=True)
        return Response(serializer.data)


class CreateJobView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        form = JobForm(request.data)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return Response({'status': 'Job created'})
        else:
            return Response({
                'status':'errors',
                'errors': form.errors
            })
    
    def put(self, request, pk):
        job = Job.objects.get(pk=pk, created_by=request.user)
        form = JobForm(request.data, instance=job)

        try:
            form.save()
            return Response({'status': 'Updated'})
        except Exception as e:
            print(e)
            return Response({'status': 'Error'})

    
    def delete(self, request, pk):
        job = Job.objects.get(pk=pk, created_by = request.user)
        job.delete()

        return Response({'status': 'deleted'})
