from .views import CounterView
from django.urls import path


urlpatterns = [
    path(
        'counter/',
        CounterView.as_view(),
        name='counter-ip'
    )
]
