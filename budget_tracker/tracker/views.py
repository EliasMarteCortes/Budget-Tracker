from django.shortcuts import render
from django.db.models import Sum
from .models import Transaction

def dashboard(request):
    transactions = Transaction.objects.all()

    total_income = (
        transactions
        .filter(transaction_type='income')
        .aggregate(total=Sum('amount'))['total'] or 0
    )

    total_expense = (
        transactions
        .filter(transaction_type='expense')
        .aggregate(total=Sum('amount'))['total'] or 0
    )

    balance = total_income - total_expense

    category_totals = (
        transactions
        .filter(transaction_type='expense')
        .values('category__name')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )

    context = {
        'transactions': transactions[:10],
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'category_totals': category_totals,
    }

    return render(request, 'tracker/dashboard.html', context)