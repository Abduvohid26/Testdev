from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='logout'),
    path('add_yourself/', views.AddYourSelfView.as_view(), name='add_yourself'),
    path('add_yourself/<uuid:id>/', views.AddYourSelfDetailView.as_view(), name='add_yourself_detail'),
    path('add_author/', views.AddAuthorView.as_view(), name='add_author'),
    path('add_author/<uuid:id>/', views.AddAuthorDetailView.as_view(), name='add_author_detail'),
    path('paper/info/', views.PaperInformationView.as_view(), name='paper_info'),
    path('paper/info/<uuid:id>/', views.PaperInformationDetailView.as_view(), name='paper_info_detail'),
]