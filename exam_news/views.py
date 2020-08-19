from django.shortcuts import render,redirect
from newsapi import NewsApiClient
from exam_news.models import Teacher, Stud, TecherData,Teacher_Quiz_Questions,Teacher_Quiz_text,StudentSubmitQuiz
from django.contrib import messages


def news(request):
    newsapi = NewsApiClient(api_key="7f151344fc4d420b9570773b11af7cd1")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')


    articles = topheadlines['articles']

    desc = []
    hdline = []
    img = []
    date = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        hdline.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(myarticles['publishedAt'])
        ur.append(myarticles['url'])

    mylist = zip(hdline, desc, img, date,ur)

#Other News..............................................

    newsapi = NewsApiClient(api_key="7f151344fc4d420b9570773b11af7cd1")
    topheadlines = newsapi.get_top_headlines(sources='News24')


    articles = topheadlines['articles']

    desc = []
    hdline = []
    img = []
    date = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        hdline.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(myarticles['publishedAt'])
        ur.append(myarticles['url'])

    mylist1 = zip(hdline, desc, img, date,ur)


#Other News..............................................

    newsapi = NewsApiClient(api_key="7f151344fc4d420b9570773b11af7cd1")
    topheadlines = newsapi.get_top_headlines(sources='the-verge')


    articles = topheadlines['articles']

    desc = []
    hdline = []
    img = []
    date = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        hdline.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(myarticles['publishedAt'])
        ur.append(myarticles['url'])

    mylist2 = zip(hdline, desc, img, date,ur)


#Other News..............................................

    newsapi = NewsApiClient(api_key="7f151344fc4d420b9570773b11af7cd1")
    topheadlines = newsapi.get_top_headlines(sources='ESPN')


    articles = topheadlines['articles']

    desc = []
    hdline = []
    img = []
    date = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        hdline.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(myarticles['publishedAt'])
        ur.append(myarticles['url'])

    mylist3 = zip(hdline, desc, img, date,ur)


    return render(request, 'news.html', context={"mylist":mylist,"mylist1":mylist1,"mylist2":mylist2,"mylist3":mylist3})



# def bbc(request):
#     newsapi = NewsApiClient(api_key="YOUR API KEY")
#     topheadlines = newsapi.get_top_headlines(sources='bbc-news')


#     articles = topheadlines['articles']

#     desc = []
#     hdline = []
#     img = []

#     for i in range(len(articles)):
#         myarticles = articles[i]

#         news.append(myarticles['title'])
#         desc.append(myarticles['description'])
#         img.append(myarticles['urlToImage'])


#     mylist = zip(news, desc, img)


#     return render(request, 'bbc.html', context={"mylist":mylist})

def teacher(request):
    if request.method =='POST':

        if 'bsubmit' in request.POST:

            giventime = request.POST.get('timelimit')
            sub = request.POST.get('sub_name')
            bestwish = request.POST.get('bestwishes')
            warningmessage = request.POST.get('warningmsg')

            if giventime and sub: 
                 #To store into database if every conditions are satisfy     
                teacher_data = Teacher(timeslot=giventime,subject=sub,bestwish=bestwish,warningmessage=warningmessage)
                teacher_data.save()
                messages.success(request, 'Data Submitted Successfully!')
                return redirect("teacher")
            else:    
                messages.warning(request, 'Time-limitation and Subject Field Both are Required!')
                return redirect("teacher")

        if 'qsubmit' in request.POST:

            writnquestn = request.POST.get('written_question')
            imgqstn = request.FILES.get('imagequestion', False) # To prevent submitting image if there is no image choosen
            optn1 = request.POST.get('op1')
            optn2 = request.POST.get('op2')
            optn3 = request.POST.get('op3')
            optn4 = request.POST.get('op4')

            if optn1 and optn2 and optn3 and optn4:
                 #To store into database if every conditions are satisfy     
                teacher_data1 = TecherData(writtenquestion=writnquestn,imagequestion=imgqstn,option1=optn1,option2=optn2,option3=optn3,option4=optn4)
                teacher_data1.save()
                messages.success(request, 'Successfully Submitted!')
                return redirect("teacher")
            else:
                messages.warning(request, 'All The Options are Required!')
                return redirect("teacher")
                
    return render(request, 'teacher.html')
            

def student(request,post_id=None):

    stname = request.GET.get('stdntname')
    if request.method == 'POST':

        st=request.POST.getlist('examsubmit')  # returns a list of values after getting from input with same name... 
        result = Stud(answer=st)
        result.save()
        messages.success(request, 'Thank You! Your Response Have Been Recorded.')
        return redirect("dashboard")

    teach = Teacher.objects.all().last()
    teachQ = TecherData.objects.all()  # [::-1] for showing in reverse order
    return render(request, 'student.html', {'teach':teach, 'teachQ':teachQ})

def deleteQuestn(request,post_id=None):
    post_to_delete=TecherData.objects.get(id=post_id)
    post_to_delete.delete()
    messages.success(request, "Question Deleted Successfully")
    
    return redirect('/student')    
    

#Quiz question section......................


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

            if optn1 and optn2 and optn3 and optn4:
                 #To store into database if every conditions are satisfy     
                teacher_data1 = Teacher_Quiz_Questions(writtenquestion=writnquestn,imagequestion=imgqstn,option1=optn1,option2=optn2,option3=optn3,option4=optn4)
                teacher_data1.save()
                messages.success(request, 'Submitted Successfully!')
                return redirect("teacherquiz")
            else:
                messages.warning(request, 'All The Options are Required!')
                return redirect("teacherquiz")
                
    return render(request, 'teacherQuiz.html')

def studentqz(request,post_id=None):

    if request.method == 'POST':

        st=request.POST.getlist('exampleRadios')  # returns a list of values after getting from input with same name... 
        result = StudentSubmitQuiz(answer=st)
        result.save()
        messages.success(request, 'Thank You! Your Response Have Been Recorded.')
        return redirect("dashboard")

    teach = Teacher_Quiz_text.objects.all().last()
    teachQ = Teacher_Quiz_Questions.objects.all()  # [::-1] for showing in reverse order
    return render(request, 'studentQuiz.html', {'teach':teach, 'teachQ':teachQ})

def deleteQuestnqz(request,post_id=None):
    post_to_delete=Teacher_Quiz_Questions.objects.get(id=post_id)
    post_to_delete.delete()
    messages.success(request, "Question Deleted Successfully")
    
    return redirect('/studentqz')    