from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/autenticacao/login/'), name='home'),
    path('admin/', admin.site.urls),
    path('cursos/', include('cursos.urls')),
    path('autenticacao/', include('autenticacao.urls')),
    path('accounts/', include('allauth.urls')),   # GitHub OAuth
]
