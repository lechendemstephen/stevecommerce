from django.shortcuts import render # type: ignore
from .models import Products, Category

from django.db.models import Q  # type: ignore

from django.core.paginator import Paginator # type: ignore

# Create your views here.

def store(request): 
    all_products = Products.objects.all()
    # pagination 
    paginator = Paginator(all_products, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == "POST": 
        query = request.POST['search_query']
        query_result = Products.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(slug__icontains=query) | Q(category__name__icontains=query))
        context = {
          
            "query": query,
            "query_result": query_result,
        }
        return render(request, 'stevecommerce/pages/store.html', context)
    else: 
     

        return render(request, 'stevecommerce/pages/store.html', {
              "products": all_products,
              "page_obj": page_obj
        } )



def single_product(request, category_name, product_slug ): 
    product = Products.objects.filter( category__name = category_name, slug = product_slug)
    # filtering the category based on the products clicked
    related_product = Products.objects.filter(category__name=category_name)
   

    context = {
        "products": product,
        "single_product": related_product
    }

    return render(request, 'stevecommerce/pages/single_product.html', context)


def about(request): 

    return render(request, 'stevecommerce/pages/about.html')
