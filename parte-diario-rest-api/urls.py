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
router.register(r'otra', views.otraViewSet)
router.register(r'palpacion', views.PalpacionViewSet)
router.register(r'opcionsanitacion', views.opcionSanitacionViewSet)
router.register(r'maquinarias', views.MaquinariasViewSet)

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
    path('parteDiarioEmpresas/<int:id>/', views.ParteDiarioEmpresasViewSet.as_view())
]

if settings.DEBUG:
    urlpatterns += [
        path(
            "",
            RedirectView.as_view(pattern_name="schema-swagger-ui"),
            name="go-to-docs",
        )
    ]


# select
# 	pp.id, pe.id as empresa_id,
#     pp.fecha as fecha,
# 	pe.empresa as empresa,
# 	pe.ruc_empresa as ruc_empresa,

# 	pen.cantidad as entrada_cantidad,
# 	pen.peso_total as entrada_peso_total,
# 	pc2.categoria as entrada_categoria,
# 	pe2.tipo as entrdada_tipo,

# 	ps.cantidad as salida_cantidad,
# 	ps.causa as salida_causa,
# 	pc3.categoria as salida_categoria,
# 	ps3.salidas as salida_tipo,

# 	pl.mm_central as lluvia_mm_central,
# 	pl.mm_retiro as lluvia_mm_retiro,
# 	pl.evento as lluvia_evento,
	
# 	pr.potrero_inicial as rotacion_potrero_inicial,
# 	pr.potrero_final as rotacion_potrero_final,

# 	pr2.potrero as recorrida_potrero,
# 	pr2.observacion as recorrida_observacion,

# 	ps2.potrero as sanitacion_potrero,
# 	ps2.observacion as sanitacion_observacion,
# 	po.opcion as sanitacion_opcion,

# 	pc.trabajos_realizados as contratistas_trabajos_realizados,
# 	pc.insumos as contratistas_insumos,

# 	pr3.cantidad as recategorizacion_cantidad,
# 	pc4.categoria as recategorizacion_categoria_inicial,
# 	pc5.categoria as recategorizacion_categoria_final
	
# 	from partediario_partediario pp
# 	left join partediario_empresa pe on pp.empresa_id = pe.id
# 	left join partediario_entrada pen on pp.entrada_id = pen.id
# 	left join partediario_salida ps on pp.salida_id = ps.id
# 	left join partediario_lluvia pl on pp.lluvia_id = pl.id 
# 	LEFT join partediario_rotacion pr on pp.rotacion_id = pr.id
# 	left join partediario_recorrida pr2 on pp.recorrida_id = pr2.id
# 	left join partediario_sanitacion ps2 on pp.sanitacion_id = ps2.id 
# 	left join partediario_contratistas pc on pp.contratistas_id = pc.id
# 	left join partediario_recategorizacion pr3 on pp.recategorizacion_id = pr3.id
# 	left join partediario_categoria pc2 on pen.categoria_id = pc2.id
# 	left join partediario_categoria pc3 on pc3.id = ps.categoria_id
# 	left join partediario_entradas pe2 on pen.entradas_id = pe2.id
# 	left join partediario_salidas ps3 on ps.salidas_id = ps3.id
# 	left join partediario_opcionsanitacion po ON ps2.elemento_id = po.id
# 	left join partediario_categoria pc4 on pc4.id = pr3.categoria_inicial_id
# 	left join partediario_categoria pc5 on pc5.id = pr3.categoria_final_id 
# ;
