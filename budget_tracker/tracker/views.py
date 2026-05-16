from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Transaction, Category, Budget
from .forms import TransactionForm, CategoryForm, BudgetForm

def dashboard(request):
    transactions = Transaction.objects.all()
    budgets = Budget.objects.all()

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

    budget_status = []

    for budget in budgets:
        spent = (
            transactions
            .filter(
                transaction_type='expense',
                category=budget.category,
                date__month=budget.month,
                date__year=budget.year,
            )
            .aggregate(total=Sum('amount'))['total'] or 0
        )

        budget_status.append({
            'category': budget.category.name,
            'limit': budget.limit,
            'spent': spent,
            'over': spent > budget.limit,
        })

    context = {
        'transactions': transactions[:10],
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'category_totals': category_totals,
        'budget_status': budget_status,
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

def delete_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)

    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')

    context = {
        'object': transaction,
    }

    return render(request, 'tracker/delete_confirm.html', context)

def category_list(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    categories = Category.objects.all()

    context = {
        'categories': categories,
        'form': form,
    }

    return render(request, 'tracker/category_list.html', context)

def delete_category(request, pk):
    category = Category.objects.get(pk=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('category_list')

    context = {
        'object': category,
    }

    return render(request, 'tracker/delete_confirm.html', context)

def budget_list(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('budget_list')
    else:
        form = BudgetForm()

    budgets = Budget.objects.all()

    context = {
        'budgets': budgets,
        'form': form,
    }

    return render(request, 'tracker/budget_list.html', context)

def delete_budget(request, pk):
    budget = Budget.objects.get(pk=pk)

    if request.method == 'POST':
        budget.delete()
        return redirect('budget_list')

    context = {
        'object': budget,
    }

    return render(request, 'tracker/delete_confirm.html', context)