from django.urls import path
from api.controller import user
import api.views as view

from django.contrib import admin
urlpatterns = [
    path('post-user/', user.create_user, name='user'),
    path('signed-in/', user.fetch_user_data, name='fetch_user_data'),
    path('create-api-key/', view.view_user, name='createapikey'),
    path('admin/', admin.site.urls, name="admin")
]

    # path('put-user/<int:idNum>/', views.put_user, name='put'),
    # path('delete-user/<int:idNum>', views.delete_user, name='deleteuser'),
# publish -> any publishing options -> the html > doc
# must derive, then code the plotting of the fourier series