from django.forms import ModelForm
from django.core.exceptions import ValidationError

from product.models import Product, Version


class ProductForm(ModelForm):
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

    class meta:
        model = Product
        fields = ("name", "manufactured_at", "image")

    def clean_name(self):
        clean_name = self.cleaned_data.get("name")
        for word in self.bad_words:
            if word in clean_name:
                raise ValidationError(f"{word}- такое слово недопустимо")
        return clean_name


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = ("product", "name_version", "num_version")
