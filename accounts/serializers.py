from rest_framework import serializers
from accounts.models import Profile, Account

class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField('get_first_name')
    last_name = serializers.SerializerMethodField('get_last_name')
    phone_number = serializers.SerializerMethodField('get_phone_number')
    def get_first_name(self,obj):
        return obj.account.first_name
    def get_last_name(self,obj):
        return obj.account.last_name
    def get_phone_number(self,obj):
        return obj.account.phone_number
    class Meta:
        model = Profile
        fields = ('first_name','last_name','phone_number','visit_counter')