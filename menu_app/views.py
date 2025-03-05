from django.http import JsonResponse
from menu_app.models import IceCreamInfo
from django.shortcuts import render
from menu_app.forms import IceCreamForm,UpdateIceCreamForm
from django.views.decorators.csrf import csrf_exempt

def index_page(request):
    return render(request,'index.html')

def list_items(request):
    return render(request,'menu.html')

def get_ice_cream_data(request):
    ice_cream_list = IceCreamInfo.objects.all()
    ice_cream_items = [{
            'ice_cream_id': item.id,
            'ice_cream_flavour': item.ice_cream_flavour,
            'ice_cream_name': item.ice_cream_name,
            'ice_cream_weight': item.ice_cream_weight
        }  for item in ice_cream_list]
    return JsonResponse({"ice_cream_details":ice_cream_items})


def get_new_item(request):
    if request.method == "POST":
        form = IceCreamForm(request.POST)
        return render(request, 'add-item.html',{"form":form})
    else:
        form = IceCreamForm()
        return render(request,'add-item.html')

def add_new_item(request):
    """To add new ice cream item to the menu_app"""
    if request.method == "POST":
        form = IceCreamForm(request.POST)
        if not form.is_valid():
            return JsonResponse({"error":form.errors},status=400)
        #if form is valid
        name = form.cleaned_data['ice_cream_name']
        flavour = form.cleaned_data['ice_cream_flavour']
        weight = form.cleaned_data['ice_cream_weight']

        new_product = IceCreamInfo.objects.create(
            ice_cream_name=name,
            ice_cream_flavour=flavour,
            ice_cream_weight=weight
        )
        new_product_data = {
            'ice_cream_name': new_product.ice_cream_name,
            'ice_cream_flavour': new_product.ice_cream_flavour,
            'ice_cream_weight': new_product.ice_cream_weight
        }
        return JsonResponse(new_product_data)
    else:
        form = IceCreamForm()
        return render(request, 'add-item.html',{"form":form})

def update_item(request,item_id):
    item = IceCreamInfo.objects.get(id=item_id)
    return render(request,'update-item.html',{'item':item})

def update_item_data(request,item_id):
    if request.method == "GET":
        item = IceCreamInfo.objects.get(id=item_id)
        item_details = {
            "ice_cream_id" : item.id,
            "ice_cream_name" : item.ice_cream_name,
            "ice_cream_flavour" : item.ice_cream_flavour,
            "ice_cream_weight" : item.ice_cream_weight
        }
        return JsonResponse({"item_details":item_details})
    else:
        form = UpdateIceCreamForm(request.POST)

        if not form.is_valid():
            return JsonResponse({"error": form.errors}, status=400)

        # if form is valid
        id = form.cleaned_data['ice_cream_id']
        name = form.cleaned_data['ice_cream_name']
        flavour = form.cleaned_data['ice_cream_flavour']
        weight = form.cleaned_data['ice_cream_weight']

        item = IceCreamInfo.objects.get(id=id)

        item.ice_cream_name = name
        item.ice_cream_flavour = flavour
        item.ice_cream_weight = weight
        item.save()

        return JsonResponse({'Message':'Item Updated Successfully'})

@csrf_exempt
def delete_item(request,item_id):
    if request.method == 'DELETE':
        ice_cream_data = IceCreamInfo.objects.get(id=item_id)
        ice_cream_data.delete()
        return JsonResponse({'Message':'Ice cream Item Deleted Successfully'})