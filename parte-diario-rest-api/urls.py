from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.views.generic.base import RedirectView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from partediario import views

router = routers.DefaultRouter()
router.register(r'empresas', views.EmpresaViewSet)
router.register(r'partediarios', views.ParteDiarioViewSet)
router.register(r'inventarios', views.InventarioViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'lluvias', views.LluviaViewSet)
router.register(r'salidas', views.SalidaViewSet)
router.register(r'entradas', views.EntradaViewSet)
router.register(r'tiposalidas', views.TipoSalidaViewSet)
router.register(r'tipoentradas', views.TipoEntradaViewSet)
router.register(r'recategorizacion', views.RecategorizacionViewSet)
router.register(r'recorridas', views.RecorridaViewSet)
router.register(r'rotacion', views.RotacionViewSet)
router.register(r'contratistas', views.ContratistasViewSet)
router.register(r'sanitacion', views.SanitacionViewSet)
router.register(r'capataz', views.CapatazViewSet)
router.register(r'date', views.dateViewSet)
router.register(r'opcionsanitacion', views.opcionSanitacionViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="parte-diario-rest-api API",
        default_version="v1",
        description="Rest api para parte diario",
    ),
    public=False,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += [
        path(
            "",
            RedirectView.as_view(pattern_name="schema-swagger-ui"),
            name="go-to-docs",
        )
    ]
