from django.shortcuts import render
from Library.forms import *
from Library.models import *
import datetime

# Create your views here.
def indexView(request):
    return render(request,'index.html')

def allBooksInLibrary(request):
    records = Books_Model.objects.all()
    return render(request,'AllBooksInLibrary.html', {'allBooks':records})

def signUpView(request):
    form = Sign_Up_Form()
    if request.method=='POST':
        form = Sign_Up_Form(request.POST)
        if form.is_valid():
            form.save()
        return allBooksInLibrary(request)
    return render(request,'signUp.html', {'form':form})

def loginView(request):
    form = Login_Form()
    if request.method == 'POST':
        form = Login_Form(request.POST)
        if form.is_valid():
            email = request.POST.get('EmailAddress')
            password = request.POST.get('Password')
            records = SignUp_Model.objects.all()
            for record in records:
                if record.EmailAddress == email and record.Password == password:
                    return allBooksInLibrary(request)
    return render(request,'login.html',{'form':form})

def addBook(request):
    form = Add_Book_Form()
    if request.method == 'POST':
        form = Add_Book_Form(request.POST)
        if form.is_valid():
            form.save()
        return allBooksInLibrary(request)
    return render(request,'Add_Book.html',{'form':form})

def issueBook(request):
    form = Issue_Book_Form()
    records = Books_Model.objects.all()
    if request.method == 'POST':
        form = Issue_Book_Form(request.POST)
        if form.is_valid():
            form.save()
        return allBooksInLibrary(request)
    dictionary = {'form': form, 'allBooks': records}
    return render(request, 'Issue_Book.html', dictionary)

def returnBook(request):
    perDayFine = 50
    bookInfo = Issue_Book_Model.objects.all()
    uid = request.POST.get('UID')
    bookName = request.POST.get('BookName')
    issuedDate = ''
    fine=0
    for record in bookInfo:
        if record.UID == uid and bookName == record.BookName:
            issuedDate = record.CurrentDate
    if issuedDate != '':
        year,month,day = issuedDate.split("-")
        dateDifference = abs(int(day) - datetime.now().day)

        print("\n--- dateDifference = ", dateDifference)

        if dateDifference > 15:
            fine = (dateDifference - 15) * perDayFine

def updateBookView(request, id):
    item = Books_Model.objects.get(id=id)
    form = UpdateForm(instance=item)
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            item = Books_Model.objects.get(id=id)
            form = UpdateForm(request.POST, instance=item)
            form.save()
            return allBooksInLibrary(request)
    return render(request,'Update.html',{'form':form})

def deleteBookView(request,id):
    record = Books_Model.objects.get(id=id)
    form = DeleteForm(instance=record)
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            record = Books_Model.objects.get(id=id)
            record.delete()
            return allBooksInLibrary(request)
    return render(request,'Delete.html',{'form':form})





