from django.urls import path
from rango import views

app_name = 'rango'



urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('category/<slug:category_name_slug>/',
         views.ShowCategory.as_view(), name='show_category'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('category/<slug:category_name_slug>/add_page/',
         views.AddPageView.as_view(), name='add_page'),
    path('restricted/', views.restricted, name='restricted'),
    path('register_profile/', views.RegisterProfileView.as_view(),
         name='register_profile'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
]