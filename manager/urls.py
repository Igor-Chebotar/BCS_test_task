from django.contrib import admin
from django.urls import path

from .views import TransactionsView, TransactionDescriptionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TransactionsView.as_view()),
    path('<int:pk>', TransactionDescriptionView.as_view()),
]