from django.contrib import admin
from django.urls import path
from post.views import hello, goodbye, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/', hello),
    path('goodbye/', goodbye),
    path('', index)
    
]