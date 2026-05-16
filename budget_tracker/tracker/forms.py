from django import forms
from .models import Transaction, Category, Budget

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'transaction_type', 'category', 'date', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={'rows': 3}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'limit', 'month', 'year']

    def clean_month(self):
        month = self.cleaned_data['month']

        if month < 1 or month > 12:
            raise forms.ValidationError('Month must be between 1 and 12.')

        return month

    def clean_year(self):
        year = self.cleaned_data['year']

        if year < 2000:
            raise forms.ValidationError('Year must be 2000 or later.')

        return year