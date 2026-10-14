from django.shortcuts import render,redirect
from app.forms import EmployeeForm
from app.models import Employee
# Create your views here.
def home(request):
    employees=Employee.objects.all()
    return render(request,'app/home.html',{'employees':employees})

def detail(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'app/employee_detail.html',{'employee':employee})

def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_success')
    else:
        form = EmployeeForm()

    return render(request, 'app/add_employee.html', {'form': form})
def success_view(request):
    return render(request,'app/success.html')