from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin', admin.site.urls),

    path('', views.inicial, name='inicial'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutButton, name='logout'),
    path('registro', views.registro, name='registro'),
    path('token', views.tokenSent, name='token'),
    path('verify/<token>', views.verifyToken, name='verify'),
    path('esqueci-senha', views.esqueciSenha, name='esqueci-senha'),
  
    path('home', views.home, name='home'),

    path('forum/<str:pk>', views.forum, name='forum'),
    path('forum-creation', views.forumCreation, name='forum-creation'),
    path('deletar-forum/<str:pk>', views.deletarForum, name='deletar-forum'),
    path('editar-forum/<str:pk>', views.editarForum, name='editar-forum'),
    path('answer-comments/<str:pk>', views.answer_comments, name='answer-comments'),

    path('resposta/<str:pk>', views.resposta, name='resposta'),
    path('melhor-resposta/<str:forum_pk>/<str:answer_pk>', views.melhorResposta, name='melhor-resposta'),

    path('profile/<str:pk>', views.profile, name='profile'),

    path('erro', views.erroPagina, name='erro'),

    path('configuracoes', views.configuracoes, name='configuracoes'),

    path('ini2', views.ini2, name='ini2'),
]
