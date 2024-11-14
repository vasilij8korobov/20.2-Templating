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


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = ("product", "name_version", "num_version")
