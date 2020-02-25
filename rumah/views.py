from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rumah.serializers import RumahSerializer
import json

# Create your views here.
listing_property = [
        {
            "id":1,
            "title":"Rumah murah di cilejit",
            "content":"Kota baru dengan area hijau dan ruang terbuka lebih dari 30% dan danau seluas 20 hektar. Modernland Cilejit menawarkan keseimbangan hidup bersama keluarga dan orang terkasih  dengan fasilitas Water Park, Theme Park, dan Edu Park. Modernland Cilejit juga menawarkan kemudahan sehari-hari dengan akses langsung ke KRL Cilejit.",
            "host":"property145.com",
            "type_property":"rumah",
            "harga":192000000

        },
        {
            "id":2,
            "title":"Apartemen Urbantown Serpong Tower 2 ",
            "content":"URBANTOWN - Serpong berlokasi di area segitiga emas Tangerang Selatan tepatnya jalan Sarua, dekat dengan BSD & Serpong sebagai Commercial and Lifestyle Area. Memiliki hunian di URBANtown - Serpong menjadikan nilai Investasi yang menguntungkan.",
            "host":"property145.com",
            "type_property":"Apartemen",
            "harga":220000000
        },
    ]
class Property145Listings(APIView):
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer,)
    
    def get(self, request, format=None):
        serializer = RumahSerializer(listing_property, many=True)
        return Response(JSONRenderer().render(serializer.data),content_type="application/json", status=200)

    def post(self, request, format=None):
        serializer = RumahSerializer(
            data=request.data
        )
        if not serializer.is_valid():            
            return Response(data=serializer.errors, status=400)

        data = serializer.validated_data.get
        message = "data not found"
        try:
            id=data('id')
            for x in listing_property:
                if x['id'] == id:
                    message = "data found"
            
        except Exception as e:
            return Response(
                data={'errors': str(e)}, status=404
            )
        return Response(
                data={'message': message}, status=200
            )
