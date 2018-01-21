# _*_ coding: utf-8 _*_
__author__ = 'cai'
__date__ = '2017/12/9 12:25'

from django.conf.urls import url, include

from courses.views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView, VideoPalyView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),

    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)$', CourseDetailView.as_view(), name="course_detail"),

    # 课程章节信息页
    url(r'^info/(?P<course_id>\d+)$', CourseInfoView.as_view(), name="course_info"),

    # 课程评论
    url(r'^comment/(?P<course_id>\d+)$', CommentsView.as_view(), name="course_comment"),

    # 添加课程评论
    url(r'^add_comment/$', AddCommentsView.as_view(), name="add_comment"),

    # 视频播放
    url(r'^video/(?P<video_id>\d+)$', VideoPalyView.as_view(), name="video_play"),
]