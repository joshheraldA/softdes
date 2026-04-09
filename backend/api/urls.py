from django.urls import path
from api.controller import user


urlpatterns = [
    path('post-user/', user.create_user, name='user')

]

    # path('put-user/<int:idNum>/', views.put_user, name='put'),
    # path('delete-user/<int:idNum>', views.delete_user, name='deleteuser'),
# publish -> any publishing options -> the html > doc
# must derive, then code the plotting of the fourier series