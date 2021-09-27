from django.shortcuts import render, redirect
from django.http import HttpResponse
import nltk # test: test123
from .models import EndUser, Paragraph, ParaHistory
from .qg import Document, QuestionGenerator
from django.contrib.auth.models import User
# Create your views here.

def cleanText(string, v_type):
    if(v_type== "username"):
        v= True
        if(string.isalnum()):
            v= True
    elif(v_type== "password"):
        v= True
    if(not v): return None
    return string

def validate(username, password): # validation of user
    cd= EndUser.objects.filter(username= username)
    if(cd.count()< 1 or cd.count()> 1): return None
    c= EndUser.objects.get(username= username)
    if(c.password== password): return c
    return None

def index(request):
    options= {
        "username": None,
    }
    try:
        options["username"]= request.session["username"]
    except Exception:
        pass
    return render(request, "index.html", options)

def home(request):
    # print(request)
    options= {
        "username": None,
    }
    try:
        options["username"]= request.session["username"]
    except Exception:
        pass
    if request.method== "POST":
        if(request.POST.get("signup-btn", False)== "sign-up"): #code to register signup
            username= cleanText(request.POST.get("username"), "username")
            password= cleanText(request.POST.get("password"), "password")
            cpassword= cleanText(request.POST.get("cpassword"), "password")
            if(not username or not password): return redirect("/error/invalid_username_or_password")
            if(password!= cpassword): return redirect("/error/passwords_dont_match")
            if(EndUser.objects.filter(username= username)): return redirect("/error/user_already_exists")
            c= EndUser(username=username, password=password)
            c.save()
            request.session["username"]= user.username
        elif(request.POST.get("login-btn", False)== "let-me-in"): #code to authenticate login
            username= cleanText(request.POST.get("username"), "username")
            password= cleanText(request.POST.get("password"), "password")
            user= validate(username, password)
            if not user: return redirect("/error/invalid_username_or_password")
            request.session["username"]= user.username
            try:
                options["username"]= request.session["username"]
            except Exception:
                pass
    return render(request, "index.html", options)

def signup(request):
    options= {
        "username": None,
    }
    try:
        options["username"]= request.session["username"]
    except Exception:
        pass
    if request.method == "POST":
        pass
    return render(request, "signup.html", options)

def login(request):
    options= {
        "username": None,
    }
    try:
        options["username"]= request.session["username"]
    except Exception:
        pass
    return render(request, "login.html", options)

def logout(request):
    options= {
        "username": None,
    }
    try:
        options["username"]= request.session["username"]
    except Exception:
        pass
    request.session.flush()
    return redirect("/")

def error(request, err):
    options= {
        "username": None,
    }
    try:
        options["username"]= request.session["username"]
    except Exception:
        pass
    print(err)
    return render(request, "error.html", {"error_msg": err})

    # b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
    # b.save()

def questions(request):
    options= {
        "username": None,
        "text": None,
    }
    try:
        options["username"]= request.session["username"]
    except Exception:
        return redirect("/error/not_logged_in")
    
    text:str= None
    sentences= None
    questions_with_ans= None
    # print(request.POST)
    if(request.POST.get("text-area-btn-submit")== "generate-questions"):
        text= request.POST.get("text-area", None)
        # change to redirect
        if(not text): return redirect("/error/Empty Textarea")
        # All Validations Complete now processing Data
        doc= Document(text)
        sentences= doc.getPrintSentences()
        qg_maker= QuestionGenerator(doc)
        questions:dict= qg_maker.MakeQuestions()
        questions_with_ans= questions.items()
        options["text"]= text
        options["sentences"]= sentences
        options["questions_with_ans"]= questions_with_ans
        options["no_of_questions"]= len(questions_with_ans)
        if(options["username"]): # save paragraph if logged in
            user= EndUser.objects.get(username= options["username"])
            para= Paragraph(paragraph= text, no_of_questions= options["no_of_questions"])
            para.save()
            ph_query= ParaHistory.objects.filter(username= user)
            if(ph_query.count()> 0):
                ph= ParaHistory(para_no= ph_query.count()% 10, username= user, paragraph= para)
                ph.save()
            else:
                ph= ParaHistory(para_no= 0, username= user, paragraph= para)
                ph.save()
        return render(request, "questions.html", options)
    elif(request.POST.get("goback-btn")== "go-back"):
        text= request.POST.get("text-area", None)
        options["text"]= text
        return render(request, "no_questions.html", options)
    return render(request, "no_questions.html", options)


def history(request):
    options= {
        "username": None,
        "text": None,
        "paragraph": None,
    }
    try:
        options["username"]= request.session["username"]
    except Exception:
        return redirect("/error/not_logged_in")
    if(options["username"]): # get paragraph if logged in
        user= EndUser.objects.get(username= options["username"])
        ph_query= ParaHistory.objects.filter(username= user).order_by("-para_no")
        options["paragraphs"]= [p.paragraph.paragraph for p in ph_query[:10]]
    return render(request, "history.html", options)