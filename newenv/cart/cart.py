from decimal import Decimal
from django.conf import settings
from store.models import Book


#  add badr sal    from django.shortcuts import HttpResponse, render, redirect
# from django.contrib.auth import authenticate, login


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, book):
        book_id = str(book.id)
        if book.is_available() and book_id not in self.cart:
            self.cart[book_id] = {'quantity': 0, 'price': str(book.price)}
            self.cart[book_id]['quantity'] = 1
            self.save()
            return {'is_available': True}
        else:
            return {'is_available': False}

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def update(self, book, quantity):
        book_id = str(book.id)
        self.cart[book_id]['quantity'] = quantity
        
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, book):
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def __iter__(self):
        book_ids = self.cart.keys()
        books = Book.objects.filter(id__in=book_ids)
        for book in books:
            self.cart[str(book.id)]['book'] = book

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price'])for item in self.cart.values())
        # j'ai changé la fanction pour qu'elle retourne le prix total de la commande
    

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
        
