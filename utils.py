from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin

class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin


def SendOtpCode (phone_number , code):
    
    try:

        api = KavenegarAPI('654461484879414867763151587041556E574574306A63696B6B52644E3466366E56743564495A54654F633D')
        params = {
            'sender': '2000660110',#optional
            'receptor': phone_number ,#multiple mobile number, split by comma
            'message': f'your verification code is : {code}',
        } 
        response = api.sms_send(params)
        print(response)
    
    except APIException as e: 
        print(e)

    except HTTPException as e: 
        print(e)




