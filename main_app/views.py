from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CustomUserCreationForm , CaseForm, MessageForm
from .models import Case, Message
from django.http import HttpResponseForbidden

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def home_view(request):
    return render(request, 'home.html')

@login_required
def submit_case_view(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save(commit=False)
            case.user = request.user
            case.save()
            return redirect('my_cases')
    else:
        form = CaseForm()
    return render(request, 'submit_case.html', {'form': form})

@login_required
def my_cases_view(request):
    cases = Case.objects.filter(user=request.user)
    return render(request, 'my_cases.html', {'cases': cases})

@login_required
def update_case(request, case_id):
    case = get_object_or_404(Case, id=case_id, user=request.user)
    
    if case.status != 'Pending':
        return HttpResponseForbidden("You cannot update this case.")
    
    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('my_cases')
    else:
        form = CaseForm(instance=case)
    return render(request, 'update_case.html', {'form': form, 'case': case})

@login_required
def delete_case(request, case_id):
    case = get_object_or_404(Case, id=case_id, user=request.user)
    
    if case.status != 'Pending':
        return HttpResponseForbidden("You cannot delete this case.")
    if request.method == 'POST':
        case.delete()
        return redirect('my_cases')
    return render(request, 'delete_case.html', {'case': case})

@staff_member_required
def admin_dashboard(request):
    cases = Case.objects.all().order_by('-created_at')
    return render(request, 'admin_dashboard.html', {'cases': cases})

@staff_member_required
def change_case_status(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Case.STATUS_CHOICES).keys():
            case.status = new_status
            case.save()
    return redirect('admin_dashboard')
    
def about_view(request):
    return render(request, 'about.html')    

@login_required
def chat_view(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    
    if request.user != case.user and not request.user.is_staff:
        return HttpResponseForbidden("You do not have permission to view this case.")
    
    messages = case.messages.all()
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.user = request.user
            msg.case = case
            msg.save()
            return redirect('chat_view', case_id=case.id)
        
    return render(request, 'chat.html', {'case': case, 'messages': messages, 'form': form})
           

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("Sayed Hasan", "Sayed@GA.com", "Ga12345678")