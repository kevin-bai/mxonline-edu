# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View

from .models import Course
from operation.models import UserFavorite, UserCourse


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

        # 点击
        course.click_num += 1
        course.save()

        # 收藏
        fav_record_course = False
        fav_record_org = False
        if request.user.is_authenticated:
            fav_record_course = UserFavorite.objects.filter(user=request.user, fav_id=int(course_id), fav_type=1)
            if fav_record_course:
                fav_record_course = True
            fav_record_org = UserFavorite.objects.filter(user=request.user, fav_id=int(course.course_org.id),
                                                         fav_type=2)
            if fav_record_org:
                fav_record_org = True

        # 相关推荐
        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            relate_courses = []
        return render(request, 'course-detail.html', {
            'course': course,
            'relate_courses': relate_courses,
            'has_fav_course': fav_record_course,
            'has_fav_org': fav_record_org
        })


class CourseCommentView(View):
    def get(self, request, course_id):
        return render(request, 'course-comment.html')


class CourseVideoView(View):
    """
    课程章节
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        user_course = UserCourse.objects.filter(user=request.user, course=course)
        if not user_course:
            user_course = UserCourse()
            user_course.user = request.user
            user_course.course = course
            user_course.save()

        all_lesson = course.lesson_set.all()
        all_resource = course.courseresource_set.all()

        return render(request, 'course-video.html', {
            'course': course,
            'all_lesson': all_lesson,
            'all_resource': all_resource
        })
