from django.urls import path
from . import views


urlpatterns = [
    path('',views.connexion ,name="connexion"),
    path('registre',views.registre, name="registre"),
    path('index',views.index, name='index'),
    path('deconnexion',views.deconnexion,name="deconnexion"),
    # path('profil', views.profil, name="profil"),
    path('<int:user_id>/', views.details, name="details"),
    path('graph', views.graph, name="graph"),
    path('stat2',views.stat2, name="stat2"),
    path('stat3',views.stat3, name="stat3"),
    path('stat4',views.stat4, name="stat4"),
    path('home',views.other_user, name="home"),
    path('update/<int:id>',views.update_info, name="update"),
    path('detail',views.detail, name="detail"),
    path('export',views.export_data, name="export"),
]