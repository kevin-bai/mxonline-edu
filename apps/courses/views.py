# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View

from .models import Course


# Create your views here.


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by('-add_time')
        # 排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_courses = all_courses.order_by('-student_num')
            elif sort == 'hot':
                all_courses = all_courses.order_by('-click_num')
        hot_courses = all_courses.order_by('-click_num')[:3]
        return render(request, 'course-list.html', {
            'all_course': all_courses,
            'hot_course': hot_courses,
            'sort': sort
        })


class CourseDetailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course.click_num += 1
        course.save()
        return render(request, 'course-detail.html', {
            'course': course
        })


class CourseCommentView(View):
    def get(self, request, course_id):
        return render(request, 'course-comment.html')


class CourseVideoView(View):
    def get(self, request, course_id):
        return render(request, 'course-video.html')
