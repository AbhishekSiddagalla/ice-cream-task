from django.urls import path
from menu_app import views

urlpatterns = [
    path('menu/',views.list_items, name ='icecream_item_list'), #URL
    path('menu-data/',views.get_ice_cream_data,name='menu_data'), # menu API URL
    path('new-item/',views.get_new_item,name='new_item_data'), #URL
    path('add-item/',views.add_new_item, name = 'add_new_icecream_item'), # add item API URL
    path('index/',views.index_page, name='index_page'), #URL
    path('update/<int:item_id>/',views.update_item, name='update_item'), #URL
    path('update-data/<int:item_id>/',views.update_item_data,name='update_item_data'), #API URL
    path('delete/<int:item_id>/',views.delete_item,name="delete_item"),
]
