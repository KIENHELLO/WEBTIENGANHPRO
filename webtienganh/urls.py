# webtienganh/urls.py

from django.contrib import admin
from django.urls import path, include, re_path
from .views import FrontendAppView  # ← dòng này quan trọng
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vocabulary/', include('vocabulary.urls')),
    path('api/reading/', include('reading.urls')),
    path('api/writing/', include('writing.urls')),
    path('api/testcenters/', include('testcenter.urls')),
    path('api/auth/', include('users.urls')),
    path('', lambda request: HttpResponse("✅ Django backend is running successfully on Render!")),
    # Trả về index.html cho các route frontend
    re_path(r'^.*$', FrontendAppView.as_view()),  # ← dòng này sẽ xử lý mọi route còn lại
]
