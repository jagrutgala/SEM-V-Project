from django.shortcuts import render, redirect
from django.http import HttpResponse
import nltk
from .doc import Doc

# Create your views here.
def home(request):
    # print(request)
    return render(request, "index.html", {})

def error(request, err):
    print(err)
    return render(request, "error.html", {"error_msg": err})


def questions(request):
    text:str= None
    sentences= None
    questions_with_ans= None
    if(request.method== "POST"):
        if(request.POST.get("send_text-btn")== "gen_questions"):
            text= request.POST.get("edit-area", None)
            # change to redirect
            if(not text): return redirect("/error/Empty Textarea")
            # All Validations Complete now processing Data
            document= Doc(text)
            sentences= document.getCleanedSentences()
            questions:dict= document.getQuestionCandidates()
            questions_with_ans= questions.items()
            # print(questions_with_ans)
    return render(request, "questions.html", {"text": text, "sentences": sentences, "questions_a": questions_with_ans})