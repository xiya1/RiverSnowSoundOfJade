from django.urls import path,re_path
from booktest import views
#通过url函数设置url路由的配置项
#在应用的urls文件中进行url配置时需严格区别开头和结尾
urlpatterns = [
    re_path('^index/$',views.show_books),
    path('index2/',views.index2),
    # re_path('^index/(\d+)$',views.detail),
    re_path('^create$',views.create),
    re_path('^login_check$', views.login_check),
    re_path('^ajax_test$',views.ajax_test),
    re_path('^ajax_handle$',views.ajax_handle),
    re_path('^login_ajax$',views.login_ajax),
    re_path('^login_ajax_check$',views.login_ajax_check),
    re_path(r'^index1$', views.index,name='index'),
    re_path(r'^login$', views.login),
    re_path(r'^login_ajax_check$', views.login_ajax_check),
    re_path(r'^regeister$', views.regeister),
    re_path(r'^regeisterpost$', views.regeisterpost),
    re_path(r'^set_session$', views.set_session),
    re_path(r'^get_session$', views.get_session),
    re_path(r'^clear_session$', views.clear_session),
    re_path(r'^flush_session$', views.flush_session),
    re_path(r'^set_cookie$', views.set_cookie),
    re_path(r'^get_cookie$', views.get_cookie),
    re_path(r'^temp_var$', views.temp_var),
    re_path(r'^child1$', views.child),
    re_path(r'^change_pwd$', views.change_pwd), #修改密码的页面显示
    re_path(r'^change_pwd_action$',views.change_pwd_action),#修改密码的处理
    re_path(r'^verify_code$', views.verify_code),#图片验证码
    re_path(r'^url_reverse$',views.url_reverse),#url反向解析验证
    re_path(r'^show_args/(\d+)/(\d+)$',views.show_args,name='show_args'),#获取关键字参数
    re_path(r'^show_kwargs/(?P<c>\d+)/(?P<d>\d+)$',views.show_kwargs,name='show_kwargs'),#获取关键字参数
    re_path(r'^test_redirect$',views.test_redirect),#测试url反向解析函数对应的视图
    re_path(r'^static_test$',views.static_test),#测试url静态文件的配置功能
    re_path(r'^indextwo$',views.indextwo),
    re_path('^river$',views.river),
    re_path('^show_upload$',views.show_upload),#显示上传图片页面
    re_path('^upload_handle$',views.upload_handle),#上传文件后的处理
    re_path('^show_area(?P<pindex>\d*)$',views.show_area),
    re_path('^areas$',views.areas),
    re_path('^prov$',views.prov),
    re_path('^city(\d+)$',views.city),
    re_path('^dis(\d+)$',views.city),
    re_path('^set_session$',views.set_session),#设置session
    re_path('^get_session$',views.get_session),#获取session
]