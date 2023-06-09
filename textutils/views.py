# i have created this file by esan raj
from django.http import  HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def navigation(request):
    s = '''<h1> Navigation Bar<br></h1>
    <a href = "https://www.youtube.com/@esanraj1998/videos"> My own Youtube Channel</a><br>
    <a href = "https://www.instagram.com/esan_raj._/">My Instasgram</a><br>
    <a href ="https://twitter.com/smile_ishan">My twitter</a><br>
    <a href ="https://www.facebook.com/ishan.raj.92372446">My facebook</a><br>
    <a href ="https://www.linkedin.com/in/esan-raj-887207229/"></a><br>'''
    return HttpResponse(s)
def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
#     #analyse the text
    if removepunc == "on":
        if fullcaps == "on":
            if newlineremover == "on":
                punctuations = '''!()-{}[]:;'"\,<>./?@#$%^&*_~'''
                analyzed = ""
                for char in djtext:
                    if char not in punctuations:
                        if char != '\n' and char != "\r":
                            analyzed = analyzed + char.upper()
                params = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
                return render(request,'analyze.html',params)
            else:
                punctuations = '''!()-{}[]:;'"\,<>./?@#$%^&*_~'''
                analyzed = ""
                for char in djtext:
                    if char not in punctuations:
                        analyzed = analyzed + char.upper()
                params = {'purpose': 'Remove Punctuations and Capitalized', 'analyzed_text': analyzed}
                return render(request, 'analyze.html', params)
        elif newlineremover == "on":
            punctuations = '''!()-{}[]:;'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    if char != '\n' and char != "\r":
                        analyzed = analyzed + char
            params = {'purpose': 'Remove Punctuations and new line removed', 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)
        else:
            punctuations = '''!()-{}[]:;'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)
    elif(fullcaps == "on"):
        if newlineremover == "on":
            analyzed =""
            for char in djtext:
                if char != '\n' and char != "\r":
                    analyzed = analyzed + char.upper()
            params = {'purpose': 'Changed to Upper Case and new line removed', 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)
        else:
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()
            params = {'purpose': 'Capitalized', 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)
    elif newlineremover == "on":
        analyzed =""
        for char in djtext:
            if char != "\n" and char != "\r" :
                analyzed = analyzed + char
        params = {'purpose':'New Line removed','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    else:
        return HttpResponse("Error")
