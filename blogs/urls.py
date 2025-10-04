from django.urls import path
from .views import ( PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    )

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/nuevo/", PostCreateView.as_view(), name="post-new"),
    path("post/<int:pk>/editar/", PostUpdateView.as_view(), name="post-edit"), 
    path("post/<int:pk>/borrar/", PostDeleteView.as_view(), name="post-delete"),
]
