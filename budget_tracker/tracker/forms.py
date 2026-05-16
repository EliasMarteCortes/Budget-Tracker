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

    def clean_category(self):
        category = self.cleaned_data['category']

        if category is None:
            raise forms.ValidationError('Please select a category.')

        return category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class BudgetForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Budget
        fields = ['category', 'limit', 'date']
        
    def clean_date(self):
        date = self.cleaned_data['date']

        if date.year < 2000:
            raise forms.ValidationError('Year must be 2000 or later.')

        return date