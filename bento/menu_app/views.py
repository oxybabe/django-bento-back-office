
from django.shortcuts import get_object_or_404, render
from menu_app.models import Appetizer, MainCourse, Dessert



# Create your views here.

menu_list=[
      {
        "type": "appetizer",
        "price": 6.99,
        "name": "Gyoza",
        "japanese_name": "餃子",
        "description": "Delicious pan-fried dumplings filled with seasoned ground pork and vegetables. Served with a tangy soy dipping sauce."
      },
      {
        "type": "appetizer",
        "price": 5.99,
        "name": "Edamame",
        "japanese_name": "枝豆",
        "description": "Steamed young soybeans lightly seasoned with sea salt. A classic and healthy Japanese appetizer."
      },
      {
        "type": "appetizer",
        "price": 7.99,
        "name": "Agedashi Tofu",
        "japanese_name": "揚げ出し豆腐",
        "description": "Deep-fried tofu served in a flavorful dashi broth with grated daikon, green onions, and bonito flakes."
      },
      {
        "type": "appetizer",
        "price": 8.99,
        "name": "Takoyaki",
        "japanese_name": "たこ焼き",
        "description": "Savory octopus-filled batter balls cooked to perfection and topped with takoyaki sauce, mayonnaise, and bonito flakes."
      },
      {
        "type": "main course",
        "price": 12.99,
        "name": "Teriyaki Chicken",
        "japanese_name": "照り焼きチキン",
        "description": "Grilled chicken marinated in a sweet and savory teriyaki sauce. Served with steamed rice and a side of mixed vegetables."
      },
      {
        "type": "main course",
        "price": 14.99,
        "name": "Sushi Platter",
        "japanese_name": "寿司盛り合わせ",
        "description": "A delightful assortment of fresh nigiri and maki sushi. Chef's selection may include tuna, salmon, shrimp, and vegetable rolls."
      },
      {
        "type": "main course",
        "price": 15.99,
        "name": "Beef Yakiniku",
        "japanese_name": "焼肉",
        "description": "Thinly sliced beef marinated in a flavorful soy-based sauce and grilled to perfection. Served with a side of rice and kimchi."
      },
      {
        "type": "main course",
        "price": 13.99,
        "name": "Vegetable Tempura",
        "japanese_name": "野菜天ぷら",
        "description": "Assorted lightly battered and deep-fried seasonal vegetables. Served with a dipping sauce and steamed rice."
      },
      {
        "type": "main course",
        "price": 11.99,
        "name": "Tonkatsu",
        "japanese_name": "とんかつ",
        "description": "Crispy breaded and deep-fried pork cutlet served with shredded cabbage, tonkatsu sauce, and steamed rice."
      },
      {
        "type": "main course",
        "price": 16.99,
        "name": "Unagi Don",
        "japanese_name": "鰻丼",
        "description": "Grilled freshwater eel glazed with a sweet soy-based sauce. Served over a bed of steamed rice and garnished with pickles."
      },
      {
        "type": "main course",
        "price": 18.99,
        "name": "Ramen",
        "japanese_name": "ラーメン",
        "description": "A comforting bowl of flavorful broth, ramen noodles, and various toppings such as chashu pork, bamboo shoots, and a soft-boiled egg."
      },
      {
        "type": "main course",
        "price": 12.99,
        "name": "Chicken Katsu Curry",
        "japanese_name": "チキンカツカレー",
        "description": "Deep-fried breaded chicken cutlet served with Japanese curry sauce and steamed rice. A perfect combination of crispy and savory flavors."
      },
      {
        "type": "main course",
        "price": 17.99,
        "name": "Sashimi Deluxe",
        "japanese_name": "刺身デラックス",
        "description": "A premium selection of fresh sashimi, including tuna, salmon, yellowtail, and octopus. Served with wasabi, soy sauce, and pickled ginger."
      },
      {
        "type": "dessert",
        "price": 6.99,
        "name": "Matcha Green Tea Ice Cream",
        "japanese_name": "抹茶アイスクリーム",
        "description": "Creamy and refreshing matcha green tea-flavored ice cream. A perfect ending to your Japanese meal."
      },
      {
        "type": "dessert",
        "price": 7.99,
        "name": "Mochi Ice Cream",
        "japanese_name": "もちアイスクリーム",
        "description": "Chewy mochi rice cake filled with various flavors of ice cream, such as strawberry, mango, and green tea."
      },
      {
        "type": "dessert",
        "price": 5.99,
        "name": "Dorayaki",
        "japanese_name": "どら焼き",
        "description": "Sweet red bean paste sandwiched between two fluffy pancakes. A popular traditional Japanese dessert."
      }
    ]
def home(request):
    return render(request, 'home.html')
def menu(request):
 
  all_appetizers = Appetizer.objects.all()
  all_main_course = MainCourse.objects.all()
  all_desserts = Dessert.objects.all()
  print("Main Course:", all_main_course )
  
  return render(request, 'menu.html', {'menu_data':menu_list, 'appetizers': all_appetizers, 'main_course': all_main_course, 'desserts': all_desserts})

# def menu_item(request, index):
#   item = menu_list[index]
#   appetizer = Appetizer.objects.filter(type="appetizer")
#   main_course = MainCourse.objects.filter(type="main course")
#   dessert = Dessert.objects.filter(type="dessert")
#   return render(request, 'menu_item.html', {"menu_item" : item, 'appetizer': appetizer, 'main_course': main_course, 'desserts':dessert})


# def menu(request):
#     return render(request, 'menu.html', {'menu_data':menu_list} )



# def menu_item(request, index):
#   item = menu_list[index]
#   appetizer = Appetizer.objects.filter(type="appetizer")
#   main_course = MainCourse.objects.filter(type="main course")
#   dessert = Dessert.objects.filter(type="dessert")
#   return render(request, 'menu_item.html', {"menu_item" : item, 'appetizer': appetizer, 'main_course': main_course, 'desserts':dessert})


# def menu(request):
#     return render(request, 'menu.html', {'menu_data':menu_list} )

def menu_item(request, index):
  item = menu_list[index]
  return render(request, 'menu_item.html', {'menu_item' : item} )


def seed(request):
    appetizers = [
    Appetizer(name="Gyoza", japanese_name="野菜天ぷら", price= 5.99, description="Delicious pan-fried dumplings filled with seasoned ground pork and vegetables. Served with a tangy soy dipping sauce."),
    Appetizer(name="Edamame", japanese_name="枝豆", price= 5.99, description="Steamed young soybeans lightly seasoned with sea salt. A classic and healthy Japanese appetizer."), 
    Appetizer(name="Agedashi Tofu", japanese_name="揚げ出し豆腐", price= 5.99, description="Deep-fried tofu served in a flavorful dashi broth with grated daikon, green onions, and bonito flakes."),
    Appetizer(name="Takoyaki", japanese_name="たこ焼き", price= 5.99, description="Savory octopus-filled batter balls cooked to perfection and topped with takoyaki sauce, mayonnaise, and bonito flakes."),                           
]
    Appetizer.objects.bulk_create(appetizers)
      

    main_course = [
    MainCourse(name="Teriyaki Chicken", japanese_name="照り焼きチキン", price= 5.99, description="Grilled chicken marinated in a sweet and savory teriyaki sauce. Served with steamed rice and a side of mixed vegetables."),
    MainCourse(name="Sushi Platter", japanese_name="寿司盛り合わせ", price= 5.99, description="A delightful assortment of fresh nigiri and maki sushi. Chef's selection may include tuna, salmon, shrimp, and vegetable rolls."),
    MainCourse(name="Beef Yakiniku", japanese_name="焼肉", price= 5.99,  description="Thinly sliced beef marinated in a flavorful soy-based sauce and grilled to perfection. Served with a side of rice and kimchi."), 
    MainCourse(name="Chicken Katsu Curry", japanese_name="チキンカツカレー", price= 5.99,  description="A premium selection of fresh sashimi, including tuna, salmon, yellowtail, and octopus. Served with wasabi, soy sauce, and pickled ginger.")
      
    ]
    
    MainCourse.objects.bulk_create(main_course)
    
    desserts = [
    Dessert(name="Matcha Green Tea Ice Cream", japanese_name="抹茶アイスクリーム", price= 6.99, description="Creamy and refreshing matcha green tea-flavored ice cream. A perfect ending to your Japanese meal."), 
    Dessert(name="Mochi Ice Cream", japanese_name="もちアイスクリーム", price= 6.99, description="Chewy mochi rice cake filled with various flavors of ice cream, such as strawberry, mango, and green tea."), 
    Dessert(name="Dorayaki", japanese_name="どら焼き", price= 5.99, description="Sweet red bean paste sandwiched between two fluffy pancakes. A popular traditional Japanese dessert.") 
    ]
    Dessert.objects.bulk_create(desserts)
    print("Main Course:", main_course )
    return render(request, 'food_type.html', {'appetizers': appetizers, 'main_course': main_course, 'desserts': desserts})
    


def delete_menu_item(request):
  menu_item = get_object_or_404(Appetizer,  )
  if request.method == 'DELETE':
    menu_item.delete()

def edit_menu(request):
  menu_item 

