from django.shortcuts import render
from Student.forms import StudentForm
from django.http import HttpResponse

# Create your views here.
def StudentView(request):
    form = StudentForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            print("\nform is valid")
            print("firstname = ", form.cleaned_data['firstName'])
            print("lastName = ", form.cleaned_data['lastName'])
            print("city = ", form.cleaned_data['city'],"\n")
        return render(request, 'StudentTemplate.html',{'form':form})
    else:
        return HttpResponse("Something went wrong")

def StudentDashboard(request):
    return render(request,'StudDashboard.html')