from django.urls import path
from . import views

urlpatterns = [
    # when user goes to the route "", run views.index
    path("", views.index, name='index'),
    path("test",views.test, name='test'),
    path("get_data", views.get_data, name='get_data'),
    path("send_data", views.send_data, name='send_data')

]