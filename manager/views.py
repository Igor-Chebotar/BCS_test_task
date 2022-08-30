from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from .models import Transaction
from .services import send_transaction


class TransactionsView(TemplateView):
    template_name = 'main.html'

    def get(self, request):
        transactions_data = Transaction.objects.all()
        ctx = {"transactions": transactions_data}
        return render(request, self.template_name, ctx)

    def post(self, request):
        answer = send_transaction()
        if answer:
            Transaction.objects.create(id=answer)

        return HttpResponseRedirect('http://127.0.0.1:8000/tx/')


class TransactionDescriptionView(TemplateView):
    template_name = 'description.html'

    def get(self, request, pk):
        description_data = Transaction.objects.filter(bcs_id=pk)[0]
        ctx = {"item": description_data}
        return render(request, self.template_name, ctx)




