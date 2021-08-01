from Library import views
from django.urls import path
urlpatterns = [
    path('signup', views.signUpView),
    path('login', views.loginView),
    path('add', views.addBook),
    path('issue', views.issueBook),
    path('return', views.returnBook),
    path('update/<int:id>', views.updateBookView),
    path('delete/<int:id>', views.deleteBookView),
]