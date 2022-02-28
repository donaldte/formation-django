from django.urls import path

from courses.views import Create_view, Delete_view, Detail_view, List_view, Update_view

app_name='courses'
urlpatterns = [
    path('',List_view.as_view(), name='course-list'),
    path('des',List_view.as_view(template_name="courses/course-list-des.html"), name='course-list-des'),
    path('<int:pk>/detail', Detail_view.as_view(), name='course-detail'),
    path('<int:pk>/update', Update_view.as_view(), name='course-update'),
    path('create', Create_view.as_view(), name='course-create'),
    path('<int:pk>/delete', Delete_view.as_view(), name='article-delete'),

]
