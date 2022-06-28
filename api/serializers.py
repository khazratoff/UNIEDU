from rest_framework import serializers
from users.models import Profile
from courses.models import Tags,Courses


class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields='__all__'

class tagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tags
        fields='__all__'

class ownerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'
        