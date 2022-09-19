from django.urls import path
from blog import views

urlpatterns = [
    path('', views.render_blog, name='blog'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
]