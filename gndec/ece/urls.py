"""
URL configuration for gndec project.

The `urlpatterns` list rt views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path 
from . import views

urlpatterns = [
    path("home/", views.home, name = "home"),
    path("products/", views.products, name = "products"),
    path("service/", views.service, name = "service"),
    path("contact/", views.contact, name = "contact"),
            
]
