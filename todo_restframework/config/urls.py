from django.contrib import admin
from django.urls import include, path # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/v1/', include('apis.urls')), # new
]