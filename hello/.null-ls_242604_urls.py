from django.urls import path

from hello import views
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:10],
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    path('log_message/', views.log_message, name='log_message'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('', home_list_view, name='home'),
]
