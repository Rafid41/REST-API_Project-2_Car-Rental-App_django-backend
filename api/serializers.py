# api\serializers.py
# serialize means convert model to json
from rest_framework import serializers
from .models import User, Categories, Cars, CarBookingDate


class UserSerializer(serializers.ModelSerializer):
    # pass read kora jabena
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={
            "input_type": "password",
        },
    )

    class Meta:
        model = User
        fields = ["id", "email", "password", "account_type"]

    # overwrite built-in create fn of ModelSerializer
    # validated data er moddhe email, pass etc thake
    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        account_type = validated_data["account_type"]
        # User Model er create_user fn
        user = User.objects.create_user(email, password, account_type)
        return user


################### Serialize Categories ##################


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


################### Serialize Cars ##################
class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = "__all__"


################### Serialize CarBookingDates ##################
class CarBookingDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBookingDate
        fields = "__all__"
