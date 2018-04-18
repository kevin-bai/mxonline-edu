from django.shortcuts import render
from django.views.generic.base import View

from .models import Course


# Create your views here.


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all()
        hot_courses = all_courses.order_by('-click_num')[:3]
        return render(request, 'course-list.html', {
            'all_course': all_courses,
            'hot_course': hot_courses
        })


class CourseDetailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        return render(request, 'course-detail.html', {
            'course': course
        })


class CourseCommentView(View):
    def get(self, request, course_id):
        return render(request, 'course-comment.html')


class CourseVideoView(View):
    def get(self, request, course_id):
        return render(request, 'course-video.html')
