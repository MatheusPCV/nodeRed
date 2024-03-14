from django.urls import path
from app.views import clpView, templateView

urlpatterns = [
    path("clp/", clpView.as_view()),
    path("template/", templateView.as_view())
]