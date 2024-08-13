from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('	Casablanca-Settat', '	Casablanca-Settat'),
		('	Tanger-Tétouan-Al Hoceïma', 'Tanger-Tétouan-Al Hoceïma'),
		('	L\'Oriental', '	L\'Oriental '),
		('Fès-Meknès', 'Fès-Meknès'),
		('	Rabat-Salé-Kénitra', '	Rabat-Salé-Kénitra'),
		('	Béni Mellal-Khénifra', '	Béni Mellal-Khénifra '),
		('	Marrakech-Safi', '	Marrakech-Safi'),
		('	Drâa-Tafilalet', '	Drâa-Tafilalet'),
		('	Souss-Massa', '		Souss-Massa '),
 		 ('Guelmim-Oued Noun', 'Guelmim-Oued Noun'),
		('		Laâyoune-Sakia El Hamra', '	Laâyoune-Sakia El Hamra'),
		('	Dakhla-Oued Ed-Dahab', '	Dakhla-Oued Ed-Dahab')
	)

	DISCRICT_CHOICES = (
		('Casablanca', 'Casablanca'), 
		('Salé', 'Salé'),
		('Tanger', 'Tanger'),
  		('Marrakech', 'Marrakech'), 
		('Safi', 'Safi'),
		('Meknès', 'Meknès'),
  		('Oujda', '	Oujda'), 
		('Rabat', 'Rabat'),
		('	Agadir', 'Agadir'),
  		('Autre', 'Autre')
	)

	PAYMENT_METHOD_CHOICES = (
		('paypal ', 'paypal '),
		('Visa','Visa'),
		('MasterCard','MasterCard')
	)

	region = forms.ChoiceField(choices=DIVISION_CHOICES)
	ville =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['nom', 'email', 'Telphone', 'address', 'region', 'ville', 'zip_code','date_return', 'payment_method', 'N_compte', 'transaction_id']
