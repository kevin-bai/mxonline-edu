# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse
import json

from .models import Course
from operation.models import UserFavorite, UserCourse, CourseComments


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
        course = Course.objects.get(id=int(course_id))
        if not course:
            return render(request, '404.html')

        related_courses = get_realted_courses(course)

        all_comment = CourseComments.objects.filter(course=course).order_by('-add_time')
        return render(request, 'course-comment.html', {
            'course': course,
            'page_name': 'course_comment',
            'all_comment': all_comment,
            'related_courses': related_courses
        })


class CourseVideoView(View):
    """
    课程章节
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        if not course:
            return render(request, '404.html')

        user = request.user
        if not user.is_authenticated():
            return render(request, 'login.html')

        # 用户学习了某课程
        user_course = UserCourse.objects.filter(user=request.user, course=course)
        if not user_course:
            user_course = UserCourse()
            user_course.user = request.user
            user_course.course = course
            user_course.save()

        related_courses = get_realted_courses(course, show_num=3)

        all_lesson = course.lesson_set.all()
        all_resource = course.courseresource_set.all()

        return render(request, 'course-video.html', {
            'page_name': 'course_video',
            'course': course,
            'all_lesson': all_lesson,
            'all_resource': all_resource,
            'related_courses': related_courses
        })


class AddComment(View):
    """
    用户添加课程评论
    """

    def post(self, request):
        course_id = request.POST.get('course_id', 0)
        comment = request.POST.get('comments', '')
        if not (course_id > 0 and comment):
            return JsonResponse({'status': 'failed', 'msg': u'失败'})

        user = request.user
        if not user.is_authenticated():
            return JsonResponse({'status': 'failed', 'msg': '用户未登录'})

        course_comment = CourseComments()
        course_comment.user = user
        course_comment.course = Course.objects.get(id=course_id)
        course_comment.comment = comment
        course_comment.save()

        result = {'status': 'success', 'msg': u'成功'}
        return JsonResponse(result)


def get_realted_courses(course, show_num=5):
    """
    学过该课的同学还学过哪些课程
    :param course: 课程实例
    :param show_num: 显示几个
    :return: 关联的课程
    """
    user_courses = UserCourse.objects.filter(course=course)
    user_ids = [user_course.user.id for user_course in user_courses]
    # 这里通过一个人user_id的列表，筛选所有包含列表中user_id的user_course
    all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
    course_ids = [user_course.course.id for user_course in all_user_courses]
    # 取出相关课程
    related_courses = Course.objects.filter(id__in=course_ids).order_by('-click_num')[:show_num]

    return related_courses
