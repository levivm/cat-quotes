from django.conf.urls import url

from .views import CatQuotesView

urlpatterns = [
    url(r'^quotes/?$', CatQuotesView.as_view()),
]
