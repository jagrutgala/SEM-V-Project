from django.shortcuts import render, redirect
from django.http import HttpResponse
import nltk

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
    tagged_sentences:list= None
    if(request.method== "POST"):
        if(request.POST.get("send_text-btn")== "gen_questions"):
            text= request.POST.get("edit-area", None)
            # change to redirect
            if(not text): return redirect("/error/Empty Textarea")
            sentences= nltk.sent_tokenize(text)
            tagged_sentences= []
            for i in sentences:
                words= nltk.word_tokenize(i)
                i= words
                tagged_sentences.append(nltk.pos_tag(words))
    return render(request, "questions.html", {"text": text, "sentences": sentences, "tagged": tagged_sentences})