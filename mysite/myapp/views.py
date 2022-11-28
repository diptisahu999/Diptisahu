from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp. models import *
from hospital. models import *
import random
import razorpay
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    alldoc=Docter.objects.all()
    fff={
        'alldoc':alldoc
    }
    return render(request,'index.html',fff)

def DDocter(request):
    return render(request,'DDocter.html')

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def PPatient(request):
    if request.method== "GET":
        return render (request, "PPatient.html")
    else:

        Appo.objects.create(

            name = request.POST['name'],
            email = request.POST['email'],
            date = request.POST['date'],
            amount = request.POST['amount'],
            time = request.POST['time']

        )

           
        currency = 'INR'
        amount = 50000  # Rs. 200
    
        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                        currency=currency,
                                                        payment_capture='0'))
    
        # order id of newly created order.
        razorpay_order_id = razorpay_order['id']
        callback_url = 'paymenthandler/'
    
        # we need to pass these details to frontend.
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['callback_url'] = callback_url
    
        return render(request, 'pay.html', context=context)

@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            # result = razorpay_client.utility.verify_payment_signature(
            #     params_dict)
            # if result is not None:
            amount = 20000  # Rs. 200
            try:
 
                # capture the payemt
                razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                return render(request, 'paymentsucces.html')
            except:
 
                # if there is an error while capturing payment.
                return render(request, 'paymentfail.html')
            # else:
 
            #     # if signature verification fails.
            #     return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
      
        
      
def login(request):
    if request.method=='POST':
        try:
            User.objects.get(email=request.POST['email'] , password=request.POST['password'])

            return redirect('DDocter') 
        except:
            return render(request,'login.html',{'msg':'User not found'})

    return render(request,'login.html')


def PPregister(request):
    if request.method == 'GET':
        return render(request,'PPregister.html')

    else:
        global user_data
        user_data={
            'first_name':request.POST['f_name'],
            'last_name':request.POST['l_name'],
            'email':request.POST['email'],
            'mobile':request.POST['mobile'],
            'password':request.POST['password'],
            'gender':request.POST['gender'],
            'description':request.POST['description'],

        }

        global otp
        otp=random.randint(100_000,999_999)
        subject= 'Account Registation'
        massage=f'hello {user_data["first_name"]}!! \nYour OTP is {otp}.'
        send_mail(subject,massage,settings.EMAIL_HOST_USER,[user_data['email']])
        
        return render(request,'potp.html',{'msg':'invalid OTP!!'})

def potp(request):
    if otp==int(request.POST['uotp']):
        sss=User.objects.create(
            f_name=user_data['first_name'],
            l_name=user_data['last_name'],
            email=user_data['email'],
            mobile=user_data['mobile'],
            password=user_data['password'],
            gender=user_data['gender'],
            description=user_data['description'],
       )

        sss.save()
        return render(request,'PPatient.html',{'mssg':'Account Successfully!!'})
    else:
        return render(request,'otp.html',{'mssg':'Invalid otp!!'})    

def plogin(request):
    if request.method=='POST':
        try:
            User.objects.get(email=request.POST['email'] , password=request.POST['password'])

            return redirect('PPatient') 
        except:
            return render(request,'plogin.html',{'msg':'User not found'})

    return render(request,'plogin.html')

