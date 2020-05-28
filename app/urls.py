from django.urls import path

from app.views import login, callback

urlpatterns = [
    path('login/', login, name='login'),
    path('callback/', callback, name='callback'),
    path('get_token/', )
]
