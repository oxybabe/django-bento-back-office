
from django.urls import path
from menu_app.views import appetizer_record, delete_desserts, delete_main_course, dessert_record, main_record, delete_appetizer, update_appetizer, update_dessert, update_main_course



app_name = 'menu_app'

urlpatterns = [
    
    path('appetizer_list/', appetizer_record),
    path('main_course_list/', main_record),
    path('dessert_list/', dessert_record),
    path('^delete/<int:appetizer_id>/', delete_appetizer, name='delete_appetizer'),
    path('^main_course/delete/<int:main_id>/', delete_main_course, name='delete_main_course'),
    path('^dessert/delete/<int:dessert_id>/', delete_desserts, name='delete_desserts'), 
    path('update_appetizer/<int:appetizer_id>', update_appetizer, name="update_appetizer" ),
    path('update_main_course/<int:main_id>', update_main_course, name="update_main_course" ),
    path('update_dessert/<int:dessert_id>', update_dessert, name="update_dessert" )

]
    # path('appetizer/create', create_appetizer, name='create_appetizer')
    

