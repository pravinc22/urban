from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^form/$',views.formview,name='form'),
    url(r'^career/$',views.careerview,name='career'),
    url(r'^career/job$',views.jobview,name='bengluru'),
]
