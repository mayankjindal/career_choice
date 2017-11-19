from django.conf.urls import url
from stream_select import views

app_name = 'stream_select'

urlpatterns = [url(r'^$', views.HomeView, name='home'),
               url(r'^questions/$', views.QuestionView, name='ques'),
               url(r'^result/$', views.calc, name='result'),
               ]

