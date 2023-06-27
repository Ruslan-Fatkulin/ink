from django import forms
from .models import Application, Category


class ApplicationForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'u-input u-input-rectangle', 'id': ''}),
                                label='Введите ваше имя')
    number = forms.CharField(widget=forms.NumberInput(attrs={'class': 'u-input u-input-rectangle', 'id': ''}),
                             label='Введите ваш номер')
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'u-input u-input-rectangle', 'id': ''}),
                           label='Расскажите о том что хотите заказать')
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'u-input u-input-rectangle'}),
                                      label='Выберите категорию')

    class Meta:
        model = Application
        fields = ['full_name', 'number', 'text', 'category']
