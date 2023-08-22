from django.urls import path
from .views import v_list, v_create, v_delete, v_update

urlpatterns = [
    path('', v_list),
    path('create', v_create),
    path('update/<int:laboratorio_id>/', v_update),
    path('delete/<int:laboratorio_id>/', v_delete),
]