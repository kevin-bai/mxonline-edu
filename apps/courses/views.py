from django.shortcuts import render
from django.views.generic.base import View


# Create your views here.


class CourseListView(View):
    def get(self, request):
        return render(request, 'course-list.html')


class CourseDetailView(View):
    def get(self, request):
        return render(request, 'course-detail.html')


class CourseCommentView(View):
    def get(self, request):
        return render(request, 'course-comment.html')


class CourseVideoView(View):
    def get(self, request):
        return render(request, 'course-video.html')