from django.shortcuts import render,redirect
from newsapi import NewsApiClient
from exam_news.models import Teacher, Stud, TecherData
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

def search(request):
    query = request.GET['query']
    return render(request, 'search.html',{'query':query})

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
            # optn1 = request.POST.get('op1')
            # optn2 = request.POST.get('op2')
            # optn3 = request.POST.get('op3')
            # optn4 = request.POST.get('op4')

            if writnquestn or imgqstn:
                 #To store into database if every conditions are satisfy     
                teacher_data1 = TecherData(writtenquestion=writnquestn,imagequestion=imgqstn)
                teacher_data1.save()
                messages.success(request, 'Question Submitted Successfully!')
                return redirect("teacher")
            else:
                messages.warning(request, 'Please, Question is Required!')
                return redirect("teacher")
                
    return render(request, 'teacher.html')
            

def student(request,post_id=None):

    if request.method == 'POST':

        st=request.POST.getlist('examsubmit')  # returns a list of values after getting from input with same name... 
        stname = request.POST.get('stdntname')

        result = Stud(student_name=stname,answer=st)
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
    
def faq(request):
    return render(request, 'faq.html')
#Quiz question section......................


