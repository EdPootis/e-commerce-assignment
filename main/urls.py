from django.urls import path
from main.views import show_main, add_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product, delete_product, add_product_ajax, add_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product', add_product, name = 'add_product'),
    path('xml/', show_xml, name = 'show_xml'),
    path('json/', show_json, name = 'show_json'),
    path('xml/<str:id>/', show_xml_by_id, name = 'show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name = 'show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
    path('create-product-ajax', add_product_ajax, name='add_product_ajax'),
    path('create-flutter/', add_product_flutter, name='add_product_flutter')
]   