from rest_framework import serializers
from .models import Book_info, Book_type, All_type, Computer



class ComputerSerializer(serializers.ModelSerializer):
    name_com = serializers.CharField(max_length=250)
    img_com = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    class Meta:
        model = Computer
        fields = ['name_com', 'img_com', 'status_com']
    def create(self, validated_data):
        return Computer.objects.create(
            name_com=validated_data['name_com']
        )


# class Book_typeSerializer(serializers.ModelSerializer):
#     type_book = serializers.CharField(max_length=250)
#     class Meta:
#         model = Book_type
#         fields = ['type_book']
#     def create(self, validated_data):
#         return Book_type.objects.create(
#             type_book=validated_data['type_book']
#         )

# class All_typeSerializer(serializers.ModelSerializer):
#     all_type_name = serializers.CharField(max_length=250)
#     book_type = serializers.StringRelatedField(many=True)
#     class Meta:
#         model = All_type
#         fields = ['all_type_name', 'book_type']

#     def create(self, validated_data):
#         return All_type.objects.create(
#             all_type_name=validated_data['all_type_name']
#         )


# class Book_infoSerializer(serializers.ModelSerializer):
#     isbn = serializers.CharField(max_length=250, default='SOME STRING')
#     img_book = serializers.ImageField(upload_to='static/static_dirs/images/')
#     name_book = serializers.CharField(max_length=250)
#     amount_book = serializers.IntegerField()
#     location_book = serializers.CharField(max_length=250)
#     descri_book = serializers.CharField(max_length=250)

