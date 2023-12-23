from django.urls import path
from .views import homeview, WorkView, AboutView, CategoryView

app_name = 'score'
urlpatterns = [
    path('', homeview, name="home_page"),
    path('work/', WorkView.as_view(), name="work_page"),
    path('about/', AboutView.as_view(), name="about_page"),
    path('category/', CategoryView.as_view(), name="category_page"),
]