
from django.urls import path
from menu_app.views import appetizer_record, delete_desserts, delete_main_course, dessert_record, main_record, delete_appetizer



app_name = 'menu_app'

urlpatterns = [
    
    path('appetizer_list/', appetizer_record),
    path('main_course_list/', main_record),
    path('dessert_list/', dessert_record),
    path(r'^delete/<int:appetizer_id>/$', delete_appetizer, name='delete_appetizer'),
    path(r'^delete/<int:main_course_id>/$', delete_main_course, name='delete_main_course'),
    path(r'^delete/<int:delete_id>/$', delete_desserts, name='delete_main_course')

]
    # path('appetizer/create', create_appetizer, name='create_appetizer')
    
