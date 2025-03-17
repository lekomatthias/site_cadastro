from django.shortcuts import render, redirect, redirect, get_object_or_404
from .models import Cliente, Administrador
from .forms import ClienteForm, AdminForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import AdminForm, LoginAdminForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'clientes/home.html')
    # return redirect('listar_clientes')

def login_admin(request):
    if request.method == 'POST':
        form = LoginAdminForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('listar_clientes')
        else:
            messages.error(request, "E-mail ou senha incorretos.")
    else:
        form = LoginAdminForm()
    
    return render(request, 'clientes/login_admin.html', {'form': form})

@login_required
def logout_admin(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso!")
    return redirect('home')

def cadastrar_administrador(request):
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automático após cadastro
            messages.success(request, "Administrador cadastrado com sucesso!")
            return redirect('listar_clientes')
        else:
            messages.error(request, "Erro ao cadastrar administrador. Verifique os campos.")
    else:
        form = AdminForm()
    return render(request, 'clientes/cadastrar_administrador.html', {'form': form})

# Exibe todos os clientes cadastrados
@login_required
def listar_clientes(request):
    clientes = Cliente.objects.all().order_by('nome')
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})

def listar_administradores(request):
    administradores = Administrador.objects.all()
    return render(request, 'clientes/listar_administradores.html', {'administradores': administradores})

def interacoes_cliente(request):
    return render(request, 'clientes/interacoes_cliente.html')

# Exibe o formulário de cadastro de um novo cliente
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interacoes_cliente')
    else:
        form = ClienteForm()

    return render(request, 'clientes/cadastrar_cliente.html', {'form': form})

# View para modificar um cliente
@login_required
def modificar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')  # Redireciona para a lista de clientes após salvar
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes/modificar_cliente.html', {'form': form, 'cliente': cliente})


# Exclui o cliente
@login_required
def apagar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')  # Redireciona para a lista de clientes
    return render(request, 'clientes/apagar_cliente.html', {'cliente': cliente})

@login_required
def apagar_administrador(request, email):
    if not request.user.is_superuser:  # Apenas superusuários podem deletar administradores
        messages.error(request, "Você não tem permissão para excluir administradores.")
        return redirect('listar_administradores')

    admin = get_object_or_404(Administrador, email=email)
    
    if admin == request.user:
        messages.error(request, "Você não pode excluir a si mesmo.")
        return redirect('listar_administradores')

    admin.delete()
    messages.success(request, f"Administrador {email} excluído com sucesso.")
    return redirect('listar_administradores')
