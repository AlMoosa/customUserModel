from rest_framework import serializers
from userapi.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'location', 'date_joined')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')

        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user


    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.phone_number = profile_data.get('phone_number', profile.phone_number)
        profile.location = profile_data.get('location', profile.location)
        profile.date_joined = profile_data.get('date_joined', profile.date_joined)
        profile.save()

        return instance

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile') #phone_number
        extra_kwargs = {'password': {'write_only': True}}



