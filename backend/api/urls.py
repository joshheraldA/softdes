from django.urls import path, include
from . import views 

urlpatterns = [
    path('get-user/', views.view_user, name='getuser'),
    path('put-user/<int:idNum>/', views.put_user, name='put'),
    path('delete-user/<int:idNum>', views.delete_user, name='deleteuser'),
    path('filter-user/', views.filter_user, name='filteruser')
]


# publish -> any publishing options -> the html > doc
# must derive, then code the plotting of the fourier series