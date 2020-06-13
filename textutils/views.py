# i created this file - j

from django.http import HttpResponse
from django.shortcuts import render





def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def analyze(request):
    # $$$$ TO TAKE DATA  @@@@@
    djtext = request.POST.get('text','defult')
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitalize','off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremove = request.POST.get('spaceremove','off')
    charcount = request.POST.get('charcount','off')
    purpose =''
    
    #@@@@@@ NOW CHECK WHICH CASE IS CHOOSEN BY USER @@@@@@

    
    if removepunc == 'on' or capitalize == 'on' or spaceremove == 'on' or newlineremove == 'on' or charcount == 'on':
        #####THIS CODE IS FOR REMOVE punctuations#####
        if removepunc == 'on':
            analyzed_text = ' '
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            for char in djtext:
                if char not in punctuations:
                    analyzed_text = analyzed_text + char
            djtext = analyzed_text
            purpose = purpose + 'REMOVE PUNCTUATIOJNS, '
            
        

        ####### TO CAPITALIZE THE TEXT ###
        if capitalize == 'on':
            analyzed_text = ' '
            for char in djtext:
                analyzed_text = analyzed_text + char.upper()
            djtext = analyzed_text
            purpose = purpose +'TO CAPITALIZE THE TEXT, '


        ####### TO SPACEREMOVE ######
        if spaceremove == 'on':
            analyzed_text = ""
            for index, char in enumerate(djtext):
                if not(djtext[index] == " " and djtext[index+1]==" "):
                    analyzed_text = analyzed_text + char
            djtext = analyzed_text
            purpose = purpose +'TO SPACEREMOVE, '

        ###### TO NEWLINE REMOVER ######
        if newlineremove == 'on':  
            analyzed_text = ' '  
            for char in djtext:
                if char !='\n' and char != "\r":
                    analyzed_text = analyzed_text + char
            purpose = purpose +'TO NEWLINE REMOVER'

        params = {'purpose':purpose,'analyzed_text':str(analyzed_text) }  
        
         ###### TO COUNT CHARACTER ####
        if charcount == 'on':
            count = 0
            for char in djtext:
                if char != "\n" and char != " ":
                    count = int(count) + 1
            purpose = purpose +', COUNTING CHARACTER '
            params = {'purpose':purpose,'analyzed_text':str(analyzed_text) , 'count':'THE TOTAL NUMBER OF CHARACTERS IN STRING ARE '+ str(count)}   

        return render(request,'analyze.html',params)

    else:
        return HttpResponse("Error plz retry")


