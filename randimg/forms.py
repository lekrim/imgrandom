from django import forms

class ImgSetForm(forms.Form):
    RESOLUTION_CHOICES = [
        ('320×240', '320×240'),
        ('320×480', '320×480'),
        ('800×480', '800×480'),
    ]

    AMOUNT_CHOICES = [(3*i,3*i) for i in range(1,4)] # (3, 3), (6,6), (9, 9)

    img_resolution = forms.ChoiceField(label='Resolution', choices=RESOLUTION_CHOICES)
    amount = forms.ChoiceField(choices=AMOUNT_CHOICES)