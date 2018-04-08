from django.shortcuts import render
from main.models import *
import smtplib as p

# Create your views here.


def index(request):
    return render(request,"index.html")

def get_respos(request):
    respos_lst = respos.objects.all()
    return render(request,"respos_list.html",{"respos":respos_lst})
def get_banque(request):
    content = banque_info.objects.all()[0]
    return render(request,"banque_list.html",{"content":content})

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email",None)
        s = subscriber(email=email)
        s.save()
        
    return render(request,"index.html")
def send(request):
	if (request.method == 'POST'):
		name = request.POST.get('name',None)
		about = request.POST.get('email',None)
		description = request.POST.get('message',None)
		msg ="""From: From skyteam.work@gmail.com
To: %r
MIME-Version: 1.0
Content-type: text/html
Subject: BUG repport about (%a)
<h1> Message :</h1>
<p>%s</p>

"""	% (name,about,description)	
		server = p.SMTP("smtp.gmail.com",587)
		server.starttls()
		server.login("msg.bot.22@gmail.com","frbcofclvqnittjv")
		server.sendmail("msg.bot.22@gmail.com","sky.red2212@gmail.com",msg)
        #server.lgoin("teamsky.work@gmail.com","teamskywork123")
        #server.sendmail("skytechno.work@gmail.com","sky.red2212@gmail.com",msg)
		#server.login("skytechno.work@gmail.com","skytech123")
		#server.sendmail("skytechno.work@gmail.com","sky.red2212@gmail.com",msg)
        
		
		return render(request ,'index.html')

