from rest_framework import serializers

class RumahSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    content = serializers.CharField(max_length=500)
    host = serializers.CharField(max_length=50)
    type_property = serializers.CharField(max_length=20)
    harga = serializers.IntegerField()
    
