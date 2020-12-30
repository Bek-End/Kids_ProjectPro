from django.urls import path, include
from verification.views import getPhoneNumberRegistered, getPhoneNumberRegistered_TimeBased, forgotPassword, ResetPassword

urlpatterns = [
    path("<phone>/", getPhoneNumberRegistered.as_view(), name="OTP Gen"),
    path("time_based/<phone>/", getPhoneNumberRegistered_TimeBased.as_view(), name="OTP Gen Time Based"),
    path("confirm_phone/<phone>", forgotPassword.as_view(), name="Forgot password"),
    path("reset_password/<phone>", ResetPassword.as_view(), name="Reset password")
]