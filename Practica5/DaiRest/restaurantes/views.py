from django.shortcuts import render, HttpResponse, redirect
from .models import restaurantes, Plato, Registro
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PlatoForm, RegistroForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def login(request):
    username=request.POST['username']
    password=request.POST['password']
    user1=authenticate(username=username, password=password)
    if user1:
        if user1.is_active:
            user_login(request,user1)
            return redirect('/')
    else:
        return redirect('/')

def registro(request):
    return render(request,"registro.html")

def registrado(request):
    if 'submit' in request.POST:
        nusername=request.POST['nusername']
        lastname=request.POST['lastname']
        dni=request.POST['dni']
        user=User.objects.create_user(nusername)
        user.set_password(dni)
        user.save()
        return redirect('/')
    """if request.POST:
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'insertado.html')
        else:
            print(form.errors)
    else:
        form = RegistroForm()
        return render(request,'registro.html',{'form':form})
"""
@login_required
def usuario(request):
        return render(request,"perfil.html")

@login_required
def buscar(request):
    nombre=request.POST['namer']
    item = restaurantes.find({'name': nombre})
    return render(request,"buscar.html",{'nameres':item})

@login_required
def insertado(request):
    if 'submit' in request.POST:
        namei=request.POST['name']
        lati=request.POST['lat']
        longi=request.POST['long']
        data={'location': {'coordinates': [longi, lati], 'type': 'Point'}, 'name': namei}
        restaurantes.insert(data)
        item = restaurantes.find({'name': namei})
        print(item)
        return render(request,"insertado.html")

@login_required
def insertar(request):
    return render(request,"insertar.html")

@login_required
def modificar(request):
    return render(request,"modificar.html")

@login_required
def modificado(request):
    if 'submit' in request.POST:
        oldname=request.POST['oldnameres']
        newname=request.POST['newnameres']
        newlongi=request.POST['newlong']
        newlati=request.POST['newlati']
        restaurantes.update( {'name':oldname} , {"$set": {'location': {'coordinates': [newlongi, newlati], 'type': 'Point'}, 'name': newname}} )
        return render(request,"modificado.html")

"""@login_required
def mostrar(request):
    listitem=restaurantes.find({})
    items=list(listitem)
    return render(request,"mostrar.html", {'listitem':items})"""

@login_required
def mostrar(request):
    listitem=restaurantes.find({})
    items=list(listitem)
    paginator = Paginator(items, 10)

    page = request.GET.get('page')
    listrest = paginator.get_page(page)
    return render(request, 'mostrar.html', {'listrest': listrest})

@login_required
def mostrarajax(request):
    listitem=restaurantes.find({})
    items=list(listitem)
    paginator = Paginator(items, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'mostrarajax.html', {'posts': posts})

@csrf_exempt
def lazy_load_posts(request):
    page = request.POST.get('page')
    listitem=restaurantes.find({})
    posts=list(listitem)
    results_per_page = 10
    paginator = Paginator(posts, results_per_page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(2)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    posts_html = loader.render_to_string('posts.html',{'posts': posts})
    output_data = {'posts_html': posts_html,'has_next': posts.has_next()}
    return JsonResponse(output_data)

@login_required
def logout(request):
    user_logout(request)
    return redirect("/")

@login_required
def guardarPlato(request):
    if request.POST:
        form = PlatoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'insertado.html')
        else:
            print(form.errors)
    else:
        form = PlatoForm()
        return render(request,'guarda_plato.html',{'form':form})

@login_required
def listarplatos(request):
    platos=Plato.objects.all()
    return render(request,"listar_platos.html", {'listplatos':platos})


def access_error(error):
    return "Página web no encontrada", 404
