from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    #path('hello',views.helloworld),
    path('admin', admin.site.urls),
    #path('',views.helloworld),
    path('task', views.task),
    path('',views.proj),
    path('analytics', views.anal_ytics),
    path('redirect/<slug:customname>', views.redirect_to),
    path('<slug:customname>', views.redirect_to)
]