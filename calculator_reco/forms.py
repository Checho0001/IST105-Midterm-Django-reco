from django import forms

class MathForm(forms.Form):
    input1 = forms.FloatField(label="First Number")
    input2 = forms.FloatField(label="Second Number")
    OPERATION_CHOICES = [
        ('power', 'power'),
        ('modulus', 'modulus'),
        ('average', 'average'),
        ('max', 'max'),
    ]
    operation = forms.ChoiceField(choices=OPERATION_CHOICES)
