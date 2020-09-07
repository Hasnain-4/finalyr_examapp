from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Teacher_Quiz_Questions,Teacher_Quiz_text
from django.core.paginator import Paginator
from django.contrib import messages


lst = []
answers = Teacher_Quiz_Questions.objects.all()
anslist = []

for i in answers:
    anslist.append(i.answer)

def index(request):
    obj = Teacher_Quiz_Questions.objects.all()
    count = Teacher_Quiz_Questions.objects.all().count()
    paginator = Paginator(obj,1)
    try:
        page = int(request.GET.get('page','1'))  
    except:
        page =1
    try:
        questions = paginator.page(page)
    except(EmptyPage,InvalidPage):

        questions=paginator.page(paginator.num_pages)
    
    return render(request,'studentQuiz.html',{'obj':obj,'questions':questions,'count':count})

def result(request):
    score =0
    for i in range(len(lst)):
        if lst[i]==anslist[i]:
            score +=1
    return render(request,'resultQz.html',{'score':score,'lst':lst})

    
def save_ans(request):
    ans = request.GET['ans']
    lst.append(ans)
    return HttpResponse

def welcome(request):
    lst.clear()
    return render(request,'welcomeScreenQz.html')

def teacherquiz(request):
    if request.method =='POST':

        if 'bsubmitQz' in request.POST:

            giventime = request.POST.get('timelimitQz')
            sub = request.POST.get('sub_nameQz')
            bestwish = request.POST.get('bestwishesQz')
            warningmessage = request.POST.get('warningmsgQz')

            if giventime and sub: 
                 #To store into database if every conditions are satisfy     
                teacher_data = Teacher_Quiz_text(timeslot=giventime,subject=sub,bestwish=bestwish,warningmessage=warningmessage)
                teacher_data.save()
                messages.success(request, 'Data Submitted Successfully!')
                return redirect("teacherquiz")
            else:    
                messages.warning(request, 'Time-limitation and Subject Field Both are Required!')
                return redirect("teacherquiz")

        if 'qsubmitQz' in request.POST:
                
            writnquestn = request.POST.get('written_questionQz')                
            imgqstn = request.FILES.get('imagequestionQz', False) # To prevent submitting image if there is no image choosen
            optn1 = request.POST.get('op1Qz')
            optn2 = request.POST.get('op2Qz')
            optn3 = request.POST.get('op3Qz')
            optn4 = request.POST.get('op4Qz')
            answw=request.POST.get('rightans')

            if optn1 and optn2 and optn3 and optn4 and answw:
                 #To store into database if every conditions are satisfy     
                teacher_data1 = Teacher_Quiz_Questions(writtenquestion=writnquestn,imagequestion=imgqstn,option1=optn1,option2=optn2,option3=optn3,option4=optn4,answer=answw)
                teacher_data1.save()
                messages.success(request, 'Submitted Successfully!')
                return redirect("teacherquiz")
            else:
                messages.warning(request, 'Answer & All The Options are Required!')
                return redirect("teacherquiz")
                
    return render(request, 'teacherQuiz.html')

# def studentqz(request,post_id=None):

#     teach = Teacher_Quiz_text.objects.all().last()
#     teachQ = Teacher_Quiz_Questions.objects.all()  # [::-1] for showing in reverse order
#     return render(request, 'studentQuiz.html', {'teach':teach, 'teachQ':teachQ})

# def deleteQuestnqz(request,post_id=None):
#     post_to_delete=Teacher_Quiz_Questions.objects.get(id=post_id)
#     post_to_delete.delete()
#     messages.success(request, "Question Deleted Successfully")
    
#     return redirect('/studentqz')    