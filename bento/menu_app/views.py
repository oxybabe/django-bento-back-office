
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import RequestContext
from menu_app.forms import AppetizerForm, DessertForm, MainCourseForm 
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
    return render(request, 'menu.html', {'menu_data':menu_list} )

# def backoffice(request, index):
#     appetizers = Appetizer.objects.all()
#     main_courses = MainCourse.objects.all()
#     desserts = Dessert.objects.all()
#     context = {
#         'appetizers': appetizers,
#         'main_courses': main_courses,
#         'desserts': desserts,
#     }
#     return render(request, 'admin.html', context)
  

def menu_item(request, index):
  item = menu_list[index]
  return render(request, 'menu_item.html', {'item' : item} )

def appetizer_item(request, appetizer_item_id):
  appetizer_item = get_object_or_404(Appetizer, id=appetizer_item_id )
  return render(request, 'menu_item.html', {'item': appetizer_item})

def main_item(request, main_item_id):
  main_item = get_object_or_404(MainCourse, id=main_item_id )
  return render(request, 'menu_item.html', {'item': main_item})

def dessert_item(request, dessert_item_id):
  dessert_item = get_object_or_404(Dessert, id=dessert_item_id )
  return render(request, 'menu_item.html', {'item': dessert_item})


def appetizer_record(request):
  appetizer_list = Appetizer.objects.all()
  return render(request, 'office.html', {'appetizer_list': appetizer_list})

def main_record(request):
  main_course_list = MainCourse.objects.all()
  return render(request, 'office.html', {'main_course_list': main_course_list})

def dessert_record(request):
  dessert_list = Dessert.objects.all()
  return render(request, 'office.html', {'dessert_list': dessert_list})


  



def seed(request):
  if not Appetizer.objects.exists():
    appetizers = [
      Appetizer(name="Gyoza", japanese_name="野菜天ぷら", price= 5.99, description="Delicious pan-fried dumplings filled with seasoned ground pork and vegetables. Served with a tangy soy dipping sauce."),
      Appetizer(name="Edamame", japanese_name="枝豆", price= 5.99, description="Steamed young soybeans lightly seasoned with sea salt. A classic and healthy Japanese appetizer."), 
      Appetizer(name="Agedashi Tofu", japanese_name="揚げ出し豆腐", price= 5.99, description="Deep-fried tofu served in a flavorful dashi broth with grated daikon, green onions, and bonito flakes."),
      Appetizer(name="Takoyaki", japanese_name="たこ焼き", price= 5.99, description="Savory octopus-filled batter balls cooked to perfection and topped with takoyaki sauce, mayonnaise, and bonito flakes."),                           
]
    Appetizer.objects.bulk_create(appetizers)
  all_appetizers = Appetizer.objects.all()
      
  if not MainCourse.objects.exists():

    main_course = [
      MainCourse(name="Teriyaki Chicken", japanese_name="照り焼きチキン", price= 5.99, description="Grilled chicken marinated in a sweet and savory teriyaki sauce. Served with steamed rice and a side of mixed vegetables."),
      MainCourse(name="Sushi Platter", japanese_name="寿司盛り合わせ", price= 5.99, description="A delightful assortment of fresh nigiri and maki sushi. Chef's selection may include tuna, salmon, shrimp, and vegetable rolls."),
      MainCourse(name="Beef Yakiniku", japanese_name="焼肉", price= 5.99,  description="Thinly sliced beef marinated in a flavorful soy-based sauce and grilled to perfection. Served with a side of rice and kimchi."), 
      MainCourse(name="Vegetable Tempura", japanese_name="野菜天ぷら", price= 13.99, description="Assorted lightly battered and deep-fried seasonal vegetables. Served with a dipping sauce and steamed rice."),
      MainCourse(name="Tonkatsu", japanese_name="とんかつ", price= 11.99, description="Crispy breaded and deep-fried pork cutlet served with shredded cabbage, tonkatsu sauce, and steamed rice."),
      MainCourse(name= "Unagi Don", japanese_name="鰻丼", price= 16.99, description="Grilled freshwater eel glazed with a sweet soy-based sauce. Served over a bed of steamed rice and garnished with pickles."),
      MainCourse(name="Ramen", japanese_name="ラーメン", price= 12.99, description="A comforting bowl of flavorful broth, ramen noodles, and various toppings such as chashu pork, bamboo shoots, and a soft-boiled egg."),
      MainCourse(name="Chicken Katsu Curry", japanese_name="チキンカツカレー", price= 5.99,  description="A premium selection of fresh sashimi, including tuna, salmon, yellowtail, and octopus. Served with wasabi, soy sauce, and pickled ginger.")



        ]    
    MainCourse.objects.bulk_create(main_course)
  all_main_course = MainCourse.objects.all()

  if not Dessert.objects.exists():  
    desserts = [
      Dessert(name="Matcha Green Tea Ice Cream", japanese_name="抹茶アイスクリーム", price= 6.99, description="Creamy and refreshing matcha green tea-flavored ice cream. A perfect ending to your Japanese meal."), 
      Dessert(name="Mochi Ice Cream", japanese_name="もちアイスクリーム", price= 6.99, description="Chewy mochi rice cake filled with various flavors of ice cream, such as strawberry, mango, and green tea."), 
      Dessert(name="Dorayaki", japanese_name="どら焼き", price= 5.99, description="Sweet red bean paste sandwiched between two fluffy pancakes. A popular traditional Japanese dessert.") 
    ]
    Dessert.objects.bulk_create(desserts)
  all_desserts = Dessert.objects.all()
  return render(request, 'food_type.html', {'appetizers': all_appetizers, 'main_course': all_main_course, 'desserts': all_desserts})
    
# def create_appetizer(request):
#   form = AppetizerForm(request.POST or None)
#   if request.method == 'POST' and form.is_valid():
#     form.save()
#     print(request)
#     return render(request, 'order.html')
  # return HttpResponse("This is the create_appetizer view for GET requests.")




def delete_appetizer(request, appetizer_id):
  appetizer = get_object_or_404(Appetizer, id=appetizer_id)
  if request.method == 'POST':
    appetizer.delete()
    return render(request, 'office.html', {'appetizer':appetizer})
  else:
        return HttpResponseNotAllowed(['POST'])
      
def delete_main_course(request, main_id):
  main_course = get_object_or_404(MainCourse, id=main_id)
  if request.method == 'POST':
    main_course.delete()
    return render(request, 'office.html', {'main_course':main_course})
  else:
        return HttpResponseNotAllowed(['POST'])
      
def delete_desserts(request, dessert_id):
  dessert = get_object_or_404(Dessert, id=dessert_id)
  if request.method == 'POST':
    dessert.delete()
    return render(request, 'office.html', {'dessert':dessert})
  else:
        return HttpResponseNotAllowed(['POST'])
#https://stackoverflow.com/questions/46003056/how-to-make-delete-button-in-django      

def update_appetizer(request, appetizer_id):
  appetizer = get_object_or_404(Appetizer, id=appetizer_id)  
  if request.method == 'POST':
    form = AppetizerForm(request.POST, instance=appetizer)
    if form.is_valid():
      form.save()
      # return redirect('backoffice/appetizer_list')
    
  else:
    form = AppetizerForm(instance=appetizer)
  context = {
    'form': form,
    'appetizer_list': Appetizer.objects.all(),
  }
  return render(request, 'office.html', context )

def update_main_course(request, main_id):
  main_course = get_object_or_404(MainCourse, id=main_id)  
  if request.method == 'POST':
    form = MainCourseForm(request.POST, instance=main_course)
    if form.is_valid():
      form.save()  
  else:
    form = MainCourseForm(instance=main_course)
  context = {
    'form': form,
    'main_course_list': MainCourse.objects.all(),
  }
  return render(request, 'office.html', context )

def update_dessert(request, dessert_id):
  dessert = get_object_or_404(Dessert, id=dessert_id)  
  if request.method == 'POST':
    form = DessertForm(request.POST, instance=dessert)
    if form.is_valid():
      form.save()  
  else:
    form = DessertForm(instance=dessert)
  context = {
    'form': form,
    'dessert_list': Dessert.objects.all(),
  }
  return render(request, 'office.html', context )

# def create_appetizer(request):
#   if request.method == "POST":
#     form = AppetizerForm(request.POST)
#     if form.is_valid():
#       form.save()
    
#     return redirect('menu_app:appetizer_list')
#   else:
#     form = AppetizerForm
#     return render(request, "office.html", {"form": form})
  
def create_appetizer(request):
  if request.method == 'POST':
    form = AppetizerForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('menu_app:appetizer_list')
    
  else:
    form = AppetizerForm()
  context = {
    'form': form,
   
  }
  return render(request, 'office.html', context )
  
def create_main_course(request):
  if request.method == 'POST':
    form = MainCourseForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('main_course_list')
    
  else:
    form = MainCourseForm()
  context = {
    'form': form,
   
  }
  return render(request, 'office.html', context )

def create_dessert(request):
  if request.method == 'POST':
    form = DessertForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('dessert_list')
    
  else:
    form = DessertForm()
  context = {
    'form': form,
   
  }
  return render(request, 'office.html', context )
