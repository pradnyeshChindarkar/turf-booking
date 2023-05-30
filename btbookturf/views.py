# from turfbooking.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ground,Booking,Slot
from django.template import loader
import razorpay
import datetime

# ---------> PDF Genaration
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# ---------> PDF Genaration


# Create your views here.
def index(request):
    return render(request,'index2.html')



def bookit(request):
    ground_list = Ground.objects.all()
    slots = Slot.objects.all()
    template = loader.get_template('bookit.html')
    context={
        'allgrounds':ground_list,
        'allslots':slots,
    }
    return HttpResponse(template.render(context,request))


def available_slots(request):
    slotBooked=Booking.objects.filter(venue__name=spec_ground).values('slot__start_time','slot__end_time')
    allSlots=Slot.objects.values('start_time')
    # ***** SLOT LOGIC START******
    for slot in allSlots.values():
        is_open = True
        for booked_slot in slotBooked.values():
            if slot['id'] == booked_slot['slot_id']:
                is_open = False
                break
        if is_open:
            global avlSlots
            avlSlots=dict(slot)
            
            print("open -->", slot)
    print(avlSlots)

    # ***** SLOT LOGIC END******
    context={
            "avlSlot":avlSlots,
    }
    template = loader.get_template('bookingform.html')
    return HttpResponse(template.render(context ,request))

    
def form(request,name):
    # client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
    # payment_order = client.order.create({
    #     "amount": 500000,
    #     "currency": "INR",
    #     "payment_capture": "1",
    #     "receipt": "order_rcptid_11",    })
    # payment_order_id = payment_order['id']
    # amount = 1
    # -----------

    # generated_signature = payment_order_id + "|" + razorpay_payment_id, secret
    # print(generated_signature)

    # -----------

    # context={
    #     'amount':amount,
    #     'api_key':RAZORPAY_API_KEY,
    #     'order_id':payment_order_id,
    # }
    # template = loader.get_template('payment.html')

    # return render(request, 'payment_form.html')
    
    spec_ground = Ground.objects.get(name=name)
    slots = Slot.objects.all()
    slots1=Slot()
    slots2=Slot.objects.values('id')
    booking=Booking()
    abc1=Booking.objects.filter(venue__name=spec_ground).values('slot__id')
    
    slotBooked=Booking.objects.filter(venue__name=spec_ground).values('slot__start_time','slot__end_time')
    allSlots=Slot.objects.values('start_time')

    # ***** SLOT LOGIC ******
    avlSlots=[]
    for slot in allSlots.values():
        is_open = True
        for booked_slot in slotBooked.values():
            if slot['id'] == booked_slot['slot_id']:
                is_open = False
                break
        if is_open:
            avlSlot = slot.copy()
            avlSlots.append(avlSlot)
            print("open -->", slot)


    # ***** SLOT LOGIC ******

    # ***** FORM/PAYMENT LOGIC ******

    # if request.method == 'POST':
    #     amount = request.POST['amt']
    #     # Here you can simulate the payment process without actually charging any money.
    #     # You can use a message to indicate the success or failure of the payment.
    #     success_message = f"Payment of {amount} was successful!"
    #     failure_message = f"Payment of {amount} failed."
        # success = False # Set this to False if payment fails
        # if success:
        #     return redirect('/bookit')
        # else:
        #     return redirect('/')
    # ***** FORM/PAYMENT LOGIC ******
    
    context={
        'avlSlot':avlSlots,
        # 'slots2':abc1,
        # "slotsBook":abc,
        # 'amount':amount,
        # 'api_key':RAZORPAY_API_KEY,
        # 'order_id':payment_order_id,
        # 'amount':amount,
        # 'api_key':RAZORPAY_API_KEY,
        # 'order_id':payment_order_id,
        'selectedGround':spec_ground,
        'allslots':slots,
    }
    template = loader.get_template('bookingform.html')
    return HttpResponse(template.render(context,request))

def saveBooking(request,name):
    spec_ground = Ground.objects.get(name=name)
    context={
        # 'amount':amount,
        # 'api_key':RAZORPAY_API_KEY,
        # 'order_id':payment_order_id,
        'selectedGround':spec_ground,
        # 'allslots':slots,
    }
    if request.method=="POST":
        name1=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('contactNo')
        bookDate=request.POST.get('dateSelected')
        slotSelected=request.POST.get('slotSelected')
        start_time, end_time = slotSelected.split(' to ')
        slot=Slot.objects.get(start_time=start_time,end_time=end_time)
        desc=request.POST.get('description')
        global data
        data=name1,email,phone,bookDate,desc,slotSelected,spec_ground
        print(data)
        global insertDb
        insertDb=Booking(name=name1,book_date=bookDate,venue=spec_ground,description=desc,slot=slot)
        insertDb.save()
    
    template = loader.get_template('payment_success.html')
    return HttpResponse(template.render(context,request))


def book_receipt(request):
    x=datetime.datetime.now()
    # PDF Receipt Genertor
    buf = io.BytesIO()
    # create canvas
    c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
    # create text objects
    textob=c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 18)

    lines = []
    lines.append(x.strftime("%x"))
    lines.append("")
    lines.append("Name: "+insertDb.name)
    lines.append("Date Booked for: "+insertDb.book_date)
    lines.append("Venue: "+str(insertDb.venue))
    lines.append("Description: "+insertDb.description)
    lines.append("Slot: "+str(insertDb.slot))

    for line in lines:
        textob.textLine(text=line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    print("abc=",data)
    # PDF Receipt Genertor
    return FileResponse(buf,as_attachment=True,filename='receipt.pdf')