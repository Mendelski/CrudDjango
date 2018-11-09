from django.urls import path
from .views import home, create, update, delete

urlpatterns = [
   path('', home, name = 'home'),
   path('novo', create, name = 'create'),
   path('editar/<int:pk>', update, name = 'update'),
   path('apagar/<int:pk>', delete, name = 'delete')
]
