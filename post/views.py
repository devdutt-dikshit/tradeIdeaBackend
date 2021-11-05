from django.db.models.fields import TextField
from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from . import serializers 
from .models import *
from rest_framework.response import Response
import io
import json 
# Create your views here.


@api_view(['POST'])
@permission_classes([])
@parser_classes((JSONParser,))
def userRegister(request):
    data =request.data
    try:
        serializer = serializers.RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'detail': 'Registration Successful.'})
        else:
            return Response({'success': False, 'detail': 'Registration failed something went wrong.', 'error':serializer.errors})

    except Exception as e:
        return Response({'success': False, 'detail': 'Registration Failed!!', 'error': str(e)})


@api_view(['POST'])
def test(request):
    return Response({'status':"ok"})

@api_view(['POST'])
@parser_classes((JSONParser,))
def createTradeIdea(request):
    request.data['createdBy'] = request.user.id
    request.data['subscribedBy'] = '[]' 
    try:
        serializer = serializers.TradeIdeaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'detail': 'idea created Successful.'})
        else:
            return Response({'success': False, 'detail': 'idea creation failed something went wrong.', 'error': serializer.errors})
    except Exception as e:
        return Response({'success': False, 'detail': 'idea creation failed!!', 'error': str(e) })

@api_view(['GET'])
def fetchTradeIdea(request):
    if (request.GET.get('mypost') == '1'):
        print(request.user.id)
        data = TradeIdea.objects.filter(createdBy=request.user.id)
    else:
        data = TradeIdea.objects.all()
    try:
        print(data)
        serializer = serializers.TradeIdeaSerializer(data, many=True)
        return Response({'success': True, 'detail': serializer.data})
    except Exception as e:
        return Response({'success': False, 'detail': 'fetching trade ideas failed!!', 'error': str(e) })


@api_view(['POST'])
@parser_classes((JSONParser,))
def subscribedByIdea(request, ideaId):
    try:
        ideaInstance = TradeIdea.objects.get(id=ideaId)
        oldSubscribed = eval(ideaInstance.subscribedBy)
        if(not len(oldSubscribed)):
            ideaInstance.subscribedBy = str([request.user.id])
        else:
            oldSubscribed.append(request.user.id)
            ideaInstance.subscribedBy = str(oldSubscribed)
        ideaInstance.save()
        return Response({'success': True, 'detail': 'idea subscribed Successful.'})
    except Exception as e:
        return Response({'success': False, 'detail': 'idea subscribe failed!!', 'error': str(e) })

