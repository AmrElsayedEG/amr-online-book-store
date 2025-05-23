from django.urls import path
from .views import *

app_name = 'books'

review_list = ReviewViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy',
})

urlpatterns = [
    # List & Retrieve Books APIs
    path('list/', ListBooksAPIView.as_view(), name='list_books'),
    path('<int:id>/', RetrieveBookAPIView.as_view(), name='retrieve_book'),

    # Reviews CRUD APIs
    # path('<int:book_id>/reviews/', ListCreateReviewAPIView.as_view(), name='list_create_reviews'),
    path('<int:book_id>/reviews/', review_list, name='review-list-create')
]
