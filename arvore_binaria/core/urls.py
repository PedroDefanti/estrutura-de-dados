from django.urls import path
from . import views

app_name = 'bst'

# urls.py (no aplicativo 'core' ou o nome que você usa)

from django.urls import path
from . import views

# app_name = 'bst' # (Se você usa namespace)

urlpatterns = [
    path('', views.index, name='index'),
    # Esta é a URL para a função que você modificou
    path('initialize/', views.initialize_tree, name='initialize'), 
    path('insert/', views.insert_value, name='insert'),
    path('delete/', views.delete_value, name='delete'),
    path('search/', views.search_value, name='search'),
    path('balance/', views.balance_tree, name='balance'),
    path('get-tree/', views.get_tree, name='get_tree'),
]