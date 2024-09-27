from django.urls import path
from .apis import CreateProjectView, CreateDealView, EditDealView, GetTransferAmountView

urlpatterns = [
    path('create/', CreateProjectView.as_view()),
    path('deal-create/', CreateDealView.as_view()),
    path('deal/<int:pk>/', EditDealView.as_view()),
    path('get-transfer-rates/<int:pk>/', GetTransferAmountView.as_view())
]
