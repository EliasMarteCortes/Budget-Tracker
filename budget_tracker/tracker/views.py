from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Transaction
from .forms import TransactionForm

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

def transaction_list(request):
    transactions = Transaction.objects.all()

    context = {
        'transactions': transactions,
    }

    return render(request, 'tracker/transaction_list.html', context)

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()

    context = {
        'form': form,
        'title': 'Add Transaction',
    }

    return render(request, 'tracker/transaction_form.html', context)

def edit_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)

    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)

        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)

    context = {
        'form': form,
        'title': 'Edit Transaction',
    }

    return render(request, 'tracker/transaction_form.html', context)