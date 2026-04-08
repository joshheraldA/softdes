<<<<<<< HEAD
from django.urls import path, include
from . import views 
from .controller import firebase_api
urlpatterns = [
    path('get-user/', views.view_user, name='getuser'),
    path('put-user/<int:idNum>/', views.put_user, name='put'),
    path('delete-user/<int:idNum>', views.delete_user, name='deleteuser'),
    path('filter-user/', views.filter_user, name='filteruser'),
    path('users/', firebase_api.create_user, name='user' ),
=======
from django.urls import path
from api.controller import user



urlpatterns = [
    path('get-user/', user.get_user, name='getuser'),
    path('post-user/', user.post_user, name='postuser')
>>>>>>> 8428f2e (created a v2 of our api)
]


# publish -> any publishing options -> the html > doc
# must derive, then code the plotting of the fourier series