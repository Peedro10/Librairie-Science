from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Book, Category
from .cart import Cart

from django.conf import settings
from django.http import JsonResponse


# class Cart(object):
#     def __init__(self, request):
#         self.session = request.session
#         cart = self.session.get(settings.CART_SESSION_ID)
#         if not cart:
#             cart = self.session[settings.CART_SESSION_ID] = {}
#         self.cart = cart


#     def add(self, book):
#         book_id = str(book.id)
#         if book.is_available() and book_id not in self.cart:
#             self.cart[book_id] = {'quantity': 0, 'price': str(book.price)}
#             self.cart[book_id]['quantity'] = 1
#             self.save()
#             return {'is_available': True}
#         else:
#             return {'is_available': False}

#     def save(self):
#         self.session[settings.CART_SESSION_ID] = self.cart
#         self.session.modified = True

def cart_add(request, bookid):
    cart = Cart(request)  
    book = get_object_or_404(Book, id=bookid) 
    response_data = cart.add(book=book)
    return JsonResponse(response_data)


def cart_update(request, bookid, quantity):
	cart = Cart(request) 
	book = get_object_or_404(Book, id=bookid) 
	cart.update(book=book)
	price = (book.price)

	return render(request, 'cart/price.html', {"price":price})

def cart_remove(request, bookid):
    cart = Cart(request)
    book = get_object_or_404(Book, id=bookid)
    cart.remove(book)
    return redirect('cart:cart_details')

def total_cart(request):
	return render(request, 'cart/totalcart.html')

def cart_summary(request):

	return render(request, 'cart/summary.html')

def cart_details(request):
	cart = Cart(request)
	context = {
		"cart": cart,
	}
	return render(request, 'cart/cart.html', context)

