
from django.conf import settings
DOMAIN_NAME = 'http://127.0.0.1:8000'


def generate_dict_for_payment(transection):
    global DOMAIN_NAME
    payment_dict = {
        "store_id": settings.STORE_ID,                      #Store Id
        "signature_key": settings.SIGNATURE_KEY,            #Signature Key
        "tran_id": transection.transection_id,              #Transection Id
        "success_url": DOMAIN_NAME + settings.SUCCESS_URL,  #Transection Success URL
        "fail_url": DOMAIN_NAME + settings.FAIL_URL,        #Transection Fail URL
        "cancel_url": DOMAIN_NAME + settings.CANCEL_URL,    #Transection Cancel URL
        "amount": transection.transection_amount,           #Transection Amount
        "currency": "BDT",                                  #Transection Currency
        "desc": "Products",                                 #Product Description
        "cus_name": transection.customer_name,              #Customer Full name
        "cus_email": transection.customer_email,            #Customer Email
        "cus_add1": transection.customer_address,           #Customer Address 1
        "cus_add2": "Dhaka",                                #Customer Address 2
        "cus_city": "Dhaka",                                #Customer City
        "cus_state": "Dhaka",                               #Customer State
        "cus_country": "Bangladesh",                        #Customer Country
        "cus_phone": transection.customer_phone_no,         #Customer Phone No
        "opt_a": "None",                                    #Optional Data A
        "opt_b": "None",                                    #Optional Data B
        "opt_c": "None",                                    #Optional Data C
        "opt_d": "None"                                     #Optional Data D
    }
    return payment_dict

