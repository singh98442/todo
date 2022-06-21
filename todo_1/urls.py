from django.contrib import admin
from . import views
from django.urls import path


admin.site.site_header="Login to JobNepal"
admin.site.site_title="JobNepal"
admin.site.index_title="Welcome to JobNepal"

urlpatterns = [
    path('',views.index,name='index'),
    path('cont',views.cont,name='cont'),
    path('tasktable',views.tasktable,name='tasktable'),
    path('blog/<str:slug>',views.blog1,name='blog'),
    path('blogs',views.blogs,name='blogs'),
    path('output',views.output,name='output'),
]
