from django.conf.urls import url
from . import views
from . import views_cbv

urlpatterns = [
    url(r'^$', views.intro),
    url(r'^(?P<numbers>[\d/]*)$', views.dojo_sum),
    url(r'^excel$', views.excel_download),

    url(r'^cbv/list1/$', views_cbv.post_list1),
    url(r'^cbv/list2/$', views_cbv.post_list2),
    #url(r'^cbv/list1/$', views_cbv.post_list3),
    #url(r'^cbv/list1/$', views_cbv.excel_download),
]