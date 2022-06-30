"""epic_event URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from dj_rest_auth import urls
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import SimpleRouter

from epic_event.api.admin import admin_site
from epic_event.api.views import ContractViewSet, EventViewSet, UserViewSet

exclude_names = ["token_verify", "rest_user_details", "token_refresh"]
rest_auth_urls = [item for item in urls.urlpatterns if item.name not in exclude_names]

urlpatterns = [
    path("admin/", admin_site.urls),
    path("rest-auth/", include(rest_auth_urls)),
    path("rest-auth/signup/", include("dj_rest_auth.registration.urls")),
    path(
        "",
        include_docs_urls(schema_url="http://127.0.0.1:8000", title="API", permission_classes=[]),
    ),
    path(
        "schema/",
        get_schema_view(
            openapi.Info(title="Epic event API", default_version="v1.2"),
            public=True,
            permission_classes=[],
            url="http://127.0.0.1:8000",
        ).without_ui(cache_timeout=0),
        name="schema-json",
    ),
]

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("contracts", ContractViewSet, basename="contracts")
router.register("events", EventViewSet, basename="events")

urlpatterns += router.urls
