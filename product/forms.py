from django import forms
from django.forms import ModelForm, fields
from django.core.exceptions import ValidationError

from product.models import Product, Version


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'


class ProductForm(FormStyleMixin, ModelForm):
    bad_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    class Meta:
        model = Product
        fields = ("name", "description", "photo", "category", "purchase_price")

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        for word in self.bad_words:
            if word in name:
                self.add_error('name', ValidationError(f"{word} - такое слово недопустимо в имени"))
            if word in description:
                self.add_error('description', ValidationError(f"{word} - такое слово недопустимо в описании"))
        return cleaned_data


class VersionForm(FormStyleMixin, ModelForm):
    class Meta:
        model = Version
        fields = ("product", "name_version", "num_version", "status_version")
