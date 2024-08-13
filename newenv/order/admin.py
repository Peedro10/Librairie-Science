from django.contrib import admin
from .models import Order, OrderItem, Caisse
from django.db.models import Sum






class OrderItemList(admin.TabularInline):
	model = OrderItem
	extra = 0

class OrderList(admin.ModelAdmin):
	list_display = ['id','nom', 'created' ,'date_return', 'customer' , 'payable' , 'email', 'Telphone', 'address', 'region', 'ville', 'zip_code', 'payment_method', 'N_compte', 'totalbook', 'updated', 'paid','chekbook']
	list_filter = ['paid','nom','chekbook']
	list_editable = ['chekbook']
	search_fields = ['nom', 'email', 'Telphone']
	autocomplete_fields = ['customer']
	# exclude = ['name', 'email', 'phone']
	inlines = [OrderItemList]
	class Meta:
		Model = Order

admin.site.register(Order, OrderList)



class CaisseList(admin.ModelAdmin):
    list_display = ['id', 'checkout_day', 'date']
    fields = ['date']

    class Meta:
        model = Caisse

    def save_model(self, request, obj, form, change):
        if not obj.checkout_day:
            checkout_day = Order.objects.filter(created=obj.date).filter(paid=True).aggregate(Sum('payable'))['payable__sum'] or 0
            obj.checkout_day = checkout_day
        super().save_model(request, obj, form, change)

admin.site.register(Caisse, CaisseList)


admin.site.site_header = 'Bookstore Admin'
admin.site.site_title = 'Bookstore Admin'






