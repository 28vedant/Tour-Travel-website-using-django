from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Pakage, TourCart,Order

# Create your views here.
def index(request):
    return render(request, 'index.html')

def main(request):
    username = request.user.username
    allpakages = Pakage.objects.all()
    context={'usern':username,'allpakages':allpakages}
    return render(request, 'main.html', context)




def about(req):
    return render(req, "about.html")


def contact(req):
    return render(req, "contact.html")

def signup(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        ucpass = req.POST["ucpass"]
        context = {}

        if uname == "" or upass == "" or ucpass == "":
            context["errmsg"] = "Field can't be empty"
            return render(req, "signup.html", context)
        elif upass != ucpass:
            context["errmsg"] = "Password and confirm password doesn't match"
            return render(req, "signup.html", context)
        else:
            try:
                userdata = User.objects.create(username=uname, password=upass)
                userdata.set_password(upass)
                userdata.save()
                return redirect("/signin")
            except:
                context["errmsg"] = "User Already exists"
                return render(req, "signup.html", context)
    else:
        context = {}
        context["errmsg"] = ""
        return render(req, "signup.html", context)




def signin(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        context = {}
        if uname == "" or upass == "":
            context["errmsg"] = "Field can't be empty"
            return render(req, "signin.html", context)
        else:
            userdata = authenticate(username=uname, password=upass)
            if userdata is not None:
                login(req, userdata)
                return redirect("/")
            else:
                context["errmsg"] = "Invalid username and password"
                return render(req, "signin.html", context)
    else:
        return render(req, "signin.html")






def userlogout(request):
    logout(request)
    return render(request, 'index.html')

def aboutus(req):
    if req.user.is_authenticated:
        user = req.user
        context = {"username": user}
        return render(req, "aboutus.html", context)
    else:
        return render(req, "aboutus.html")


def contact(req):
    if req.user.is_authenticated:
        user = req.user
        context = {"username": user}
        return render(req, "contact.html", context)
    else:
        return render(req, "contact.html")
    

def india(req):
    if req.method =='GET':
        allpakages = Pakage.pakagemanger.india_list()
        context = {"allpakages":allpakages}
        return render(req, "main.html", context)
    else:
        allpakages = Pakage.objects.all()
        context = {"allpakages":allpakages}
        return render(req, "main.html", context)
    

def europe(req):
    if req.method =='GET':
        allpakages = Pakage.pakagemanger.europe_list()
        context = {"allpakages":allpakages}
        return render(req, "main.html", context)
    else:
        allpakages = Pakage.objects.all()
        context = {"allpakages":allpakages}
        return render(req, "main.html", context)
    

def thailand(req):
    if req.method =='GET':
        allpakages = Pakage.pakagemanger.thailand_list()
        context = {"allpakages":allpakages}
        return render(req, "main.html", context)
    else:
        allpakages = Pakage.objects.all()
        context = {"allpakages":allpakages}
        return render(req, "main.html", context)
    

def malaysia(req): 
    if req.method =='GET':
        allpakages = Pakage.pakagemanger.malaysia_list()
        context = {"allpakages":allpakages}
        return render(req, "main.html", context)
    else:
        allpakages = Pakage.objects.all()
        context = {"allpakages":allpakages}
        return render(req, "main.html", context)
    
from django.db.models import Q
def searchpakages(req):
    query = req.GET.get('q')
    errmsg=""
    if query:
        allpakages =Pakage.objects.filter(
            Q(pname__icontains=query) 
           
        )

        if len(allpakages) == 0:
            errmsg = "No pakages found"
    else:
        allpakages = Pakage.objects.all()

    context = {"allpakages":allpakages, "errmsg":errmsg, "query":query}
    return render(req, "main.html", context)

    

def showcart(req):
    if req.user.is_authenticated:  # Check if the user is authenticated
        username = req.user.username
        allcart = TourCart.objects.filter(userid=req.user.id)
        totalamount = 0
        for x in allcart:
            totalamount = totalamount + x.pid.pprice * x.qty

        totalitem = len(allcart)
        context = {
            'username': username,
            'allcart': allcart,
            'totalamount': totalamount,
            'totalitem': totalitem,
        }
        return render(req, "booking.html", context)
    else:
        allcart = TourCart.objects.filter(userid=req.user.id)
        totalamount = 0
        for x in allcart:
            totalamount = totalamount + x.pid.pprice * x.qty
        totalitem = len(allcart)
        context = {
            'allcart': allcart,
            'totalamount': totalamount,
            'totalitem': totalitem,
        }
        return render(req, "booking.html", context)

        
def addtocart(req,pid):
    # if req.user.is_authenticated:
    #     user = req.user
    # else:
    #     user = None

    # allpakages = get_object_or_404(Pakage, pid=pid)
    # cartitem,created = TourCart.objects.get_or_create(userid=user, pid=allpakages)
    # if not created:
    #     cartitem.qty = cartitem.qty + 1
    # else:
    #     cartitem.qty = 1
    # cartitem.save()
    # return redirect("/showcart")
    allpakages = Pakage.objects.get(pid=pid)
    user =req.user if req.user.is_authenticated else None
    if user:
       
        cartitem,created = TourCart.objects.get_or_create(userid=user, pid=allpakages)
    else :
        return redirect("/signin")
    print(cartitem.qty,created)
       
    if not created:
            cartitem.qty = cartitem.qty + 1
    else:
            cartitem.qty = 1
    cartitem.save()
    return redirect("/showcart")
    

   
        
def updateqty(req, qv, pid):
    allcart = TourCart.objects.filter(pid=pid)
    if qv == 1:
        total =allcart[0].qty + 1
        allcart.update(qty=total)
    else:
        if allcart[0].qty > 1:
            total = allcart[0].qty-1
            allcart.update(qty=total)
        else:
            allcart = TourCart.objects.filter(pid=pid)
            allcart.delete()

    return redirect("/showcart")


import razorpay

import random 
from django.conf import settings
from django.core.mail import send_mail


def payment(req):
    if req.user.is_authenticated:
        user = req.user
        client=razorpay.Client(
            auth=("rzp_test_lSV9EyJwYqxUzc","BdEutIdssDQUAp76rFITZeAi")
        )

        allcart = TourCart.objects.filter(userid=user)

        for x in allcart:
            orderid = random.randrange(1000,900000000)
            orderdata = Order.objects.create(userid=user, orderid=orderid, pid=x.pid,qty=x.qty)
            orderdata.save()
            x.delete()


        totalamount = 0 
        orderdata=Order.objects.filter(userid=user)
        for x in orderdata:
            totalamount = totalamount + x.pid.pprice * x.qty
            oid = x.orderid


        data = {
            "amount": totalamount * 100,
            "currency": "INR",
            "receipt": str(oid),
        }

        payment = client.order.create(data=data)

        subject =f"Travel-X payment done for Order Id: {oid}"
        message = f"Hi{user},Thank you for booking \n  Total Amount Paid ={totalamount}Rs/-"
        emailfrom = settings.EMAIL_HOST_USER
        receiver = [user]
        send_mail(subject, message, emailfrom, receiver)

        context = {
                'data': payment,
                'amount':payment,
                'username': user,
        }

        return render(req, "payment.html", context)
    else:
        return redirect("/signin")
    

def showbooking(req):
    if req.user.is_authenticated:
        user = req.user
        orderdata = Order.objects.filter(userid=user)
        totalamount = 0
        for x in orderdata:
            totalamount = totalamount + x.pid.pprice * x.qty

        context = {
            'username': user,
            'orderdata': orderdata,
            'totalamount': totalamount,
        }
        return render(req, 'showbooking.html', context)
    else:
        user = None
        return redirect("/signin")
    

from Tourtravelapp.forms  import Viewpakages 


def addpakages(req):

    if req.user.is_authenticated:
        user = req.user
        if req .method == 'GET':
            # Render form
            form = Viewpakages()
            context = {'form': form}
            return render(req, 'addpakage.html', context)
        else:
             # Check validity of the form and save to database
            form = Viewpakages(req.POST,req.FILES or None)
            if form.is_valid():
                # Save form data to model
                form.save()
                return redirect('/')
            else:
                # If the form is invalid, re-render the page with existing data.
                context = {'form': form,'username':user}
                return render(req, 'addpakage.html', context)
    else:
        return redirect()
    




def userdetails(request):
    users = User.objects.all()
    return render(request, 'userdetails.html', {'users': users})
    

def showpakage(req):
    if req.user.is_authenticated:
        user = req.user
        mypakages = Pakage.objects.all()
        context = {'username': user, 'mypakages': mypakages}
        return render(req, 'showpakage.html', context)
    else:
        return redirect("/signin")
    
def  updatepakage(req,pid):
    if req.user.is_authenticated:
        user = req.user
        mypakages = Pakage.objects.get(pid=pid)
        if req.method == 'POST':
            form = Viewpakages(req.POST,req.FILES or None,instance=allpakages)
            if form.is_valid():
                form.save()
                return redirect('/showpakage')
            else:
                form = Viewpakages(instance=mypakages)
            context = {'form': form,'username':user}
            return render(req, 'addpakage.html', context)

        else:  
            return redirect('/sigin')            