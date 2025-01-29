from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import ForumCreation, AnswerCreation, ProfilePictureUpdate, UserUpdateForm, ComentarioForumForm,ComentarioAnswerForm,ForumUpdate
from .models import ForumPost, Answer, Profile, Tag, Notification, ComentarioForum, ComentarioAnswer
import uuid
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth.hashers import check_password


# DECORATOR PÁGINAS QUE NÃO PODEM SER ACESSADAS POR USUÁRO LOGADO
def login_forbidden(function=None, redirect_to=None):
    actual_decorator = user_passes_test(lambda u: u.is_anonymous,
                                        login_url=redirect_to)
    if function:
        return actual_decorator(function)
    return actual_decorator


# ABERTURA
def inicial(request):
    return render(request, 'inicial2.html')


# PÁGINA DE LOGIN
@login_forbidden(redirect_to='home')
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            pass

        user = authenticate(username=username, password=password)

        if user is not None:
            profile = Profile.objects.get(user=user)
            if profile.verified:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Usuário não verificado")
        else:
            messages.error(request, "Usuário e/ou senha inválido(s)")

    return render(request, 'login.html')


# PÁGINA DE REGISTRO
@login_forbidden(redirect_to='home')
def registro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            if User.objects.filter(username=username).first():
                messages.error(request, 'Username já existe.')
                return redirect('registro')

            elif User.objects.filter(email=email).first():
                messages.error(request, 'Email já está em uso.')
                return redirect('registro')

            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()

            profile = Profile.objects.create(user=user,
                                             token=str(uuid.uuid4()))
            profile.save()

            sendEmail(email, profile.token)

            return redirect('token')

        except Exception as e:
            print(e)

    context = {}
    return render(request, 'registro.html', context)


# TOKEN SENT
@login_forbidden(redirect_to='home')
def tokenSent(request):
    context = {'hide_slides': True}
    return render(request, 'token.html', context)


# VERIFICA TOKEN
def verifyToken(request, token):
    try:
        profile = Profile.objects.filter(token=token).first()
        if profile:
            profile.verified = True
            profile.save()
            messages.success(request, 'Sua conta foi verificada.')
            return redirect('login')
        else:
            return redirect('erro')
    except Exception as e:
        print(e)


# MANDA EMAIL
def sendEmail(email, token):
    assunto = "Sua conta PUCLY precisa ser verificada"
    mensagem = f'Por favor, clique no link para verificar sua conta http://127.0.0.1:8000/verify/{token}'
    send_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(assunto, mensagem, send_from, recipient_list)


# PÁGINA PRINCIPAL
@login_required(login_url='login')
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    forums = ForumPost.objects.filter(
        Q(tags__name__icontains=q) | Q(title__icontains=q)
        | Q(text__icontains=q))

    profiles = Profile.objects.order_by('-pontos')[:10]
    tags = Tag.objects.all()
    context = {
        'forums': forums,
        'profiles': profiles,
        'tags': tags,
        'range': range(20)
    }
    return render(request, 'home.html', context)


# LOGOUT
def logoutButton(request):
    logout(request)
    return redirect('login')


# FORUM
@login_required(login_url='login')
def forum(request, pk):
    forum = ForumPost.objects.get(id=pk)
    answers = forum.answer_set.order_by('-melhor_resposta', '-created')
    tags = forum.tags.all()

    if request.method == 'POST':
        form = ComentarioForumForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.forum = forum
            comentario.user = request.user
            comentario.save()
        return redirect('forum', pk=pk)

    context = {
        'forum': forum,
        'tags': tags,
        'answers': answers,
    }
    return render(request, 'forum.html', context)

#COMENTÁRIOS RESPOSTAS
def answer_comments(request, pk):
    answer = Answer.objects.get(id=pk)
    forum = answer.forum
    if request.method == 'POST':
        form = ComentarioAnswerForm(request.POST)
        if form.is_valid():       
            comentario = form.save(commit=False)
            comentario.user = request.user
            comentario.answer = answer
            comentario.save()
        return redirect('forum', pk=forum.id)


# CRIADOR DE FORUM
@login_required(login_url='login')
def forumCreation(request):
    if request.method == 'POST':
        form = ForumCreation(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            tag = request.POST.get("tags")
            anonimo = request.POST.get("anonimo")
            forum.host = request.user
            if anonimo == "on":
                forum.anonimo = True
            else:
                forum.anonimo = False
            forum.save()
            forum.tags.add(tag)
            return redirect('forum', pk=forum.id)

    return redirect('home')


# DELETAR POSTAGEM
def deletarForum(request, pk):
    postagem = ForumPost.objects.get(id=pk)
    postagem.delete()
    return redirect('home')


# EDITAR POSTAGEM
def editarForum(request, pk):
    postagem = ForumPost.objects.get(id=pk)

    if request.method == 'POST':
        form = ForumUpdate(request.POST, instance=postagem)
        title = request.POST.get('title')
        postagem.title = title
        postagem.save()
        if form.is_valid():
          print("AAAAAAAAAAAAAAAAAAAAAAAAA")
          print("AAAAAAAAAAAAAAAAAAAAAAAAA")
          print("AAAAAAAAAAAAAAAAAAAAAAAAA")
          print("AAAAAAAAAAAAAAAAAAAAAAAAA")
          form.save()
        return redirect('home')

    return redirect('home')


# PÁGINA DE RESPOSTA
def resposta(request, pk):
    form = AnswerCreation()
    forum = ForumPost.objects.get(id=pk)

    if request.method == 'POST':
        form = AnswerCreation(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.sender = request.user
            answer.forum = forum
            answer.save()

            profile = Profile.objects.get(user=request.user)
            profile.pontos += 5
            profile.save()

            receiver = Profile.objects.get(user=forum.host)
            receiver.unread_notifications = True
            receiver.save()

        return redirect('forum', pk=pk)

    context = {'form': form, 'forum': forum}
    return render(request, "resposta.html", context)


# MARCAR MELHOR RESPOSTA
def melhorResposta(request, forum_pk, answer_pk):
    forum = ForumPost.objects.get(id=forum_pk)
    if not forum.melhor_resposta and request.user == forum.host:
        forum.melhor_resposta = True
        forum.save()

        answer = Answer.objects.get(id=answer_pk)
        answer.melhor_resposta = True
        answer.save()

        profile = Profile.objects.get(user=answer.sender)
        profile.pontos += 5
        profile.save()

    return redirect('forum', pk=forum_pk)


# PERFIL
@login_required(login_url='login')
def profile(request, pk):
    usuario = User.objects.get(id=pk)
    forums = usuario.forumpost_set.all()[:3]
    answers = usuario.answer_set.all()[:8]
    profile = Profile.objects.get(user=usuario)
    melhores = Answer.objects.filter(sender=usuario,
                                     melhor_resposta=True).count()
    context = {
        'usuario': usuario,
        'forums': forums,
        'answers': answers,
        'profile': profile,
        'melhores': melhores,
    }
    return render(request, 'profile.html', context)


# ESQUECI SENHA
@login_forbidden(redirect_to='home')
def esqueciSenha(request):
    context = {}
    return render(request, 'senha.html', context)


# ERRO
def erroPagina(request):
    context = {}
    return render(request, 'erro.html', context)


#TESTES
def ini2(request):
    return render(request, 'inicial.html')


def configuracoes(request):
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user)
    form_user = UserUpdateForm(instance=user)

    if request.method == 'POST':
        form_pp = ProfilePictureUpdate(request.POST,
                                       request.FILES,
                                       instance=profile)
        form_user = UserUpdateForm(request.POST, instance=user)
        if form_pp.is_valid() and form_user.is_valid():
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if check_password(old_password, user.password):
              if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Sua senha foi atualizada.')
              else:
                messages.error(request, "A confirmação de senha não confere.")
            else:
              messages.error(request, "Senha inválida.")
            form_pp.save()
            form_user.save()

    return render(request, 'configuracoes.html', {'form_user': form_user})
