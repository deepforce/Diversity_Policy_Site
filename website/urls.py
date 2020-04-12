from django.urls import path
from . import views
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Added call to the new (10/28) autocomplete function instead of previous one
urlpatterns = [
    path('', views.search_home, name='index_view'),
    path('policy/', views.policy_search, name='policy-search'),
    path('policy_suggest/', views.autocompleteModel, name='policy-suggest'),
<<<<<<< HEAD
    # path('about_page/', views.about_page, name='about-page'),
    # path('contribute_policy/', views.contribute_policy, name='contribute-policy')
=======
    path('about_page/', views.about_page, name='about-page'),
    path('contribute_policy/', views.contribute_policy, name='contribute-policy'),
    path('login/', views.login, name="login"),
    path('landing/', views.landing, name='landing'),
    path('signup/', views.signup, name='signup')
>>>>>>> login
]

urlpatterns += staticfiles_urlpatterns()