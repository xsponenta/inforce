from django.urls import path
from .views import CreateEmployeeView, VoteView, GetResultsView

urlpatterns = [
    path('create/', CreateEmployeeView.as_view(), name='create_employee'),
    path('vote/', VoteView.as_view(), name='vote'),
    path('results/', GetResultsView.as_view(), name='get_results'),
]