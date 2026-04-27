from django.shortcuts import render

##These three lines copied from django restframework document ##################FOR Seialization
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


#These 2 lines from app(team_players) and these two for both Seialization and DeSeialization
from team_players.models import Player_Details
from team_players.serializer import PlayerSerializer



#######This is for serialization (means converting the django object to JSON format)
@csrf_exempt
def player_list(request):
    
    ##This is for GET Request
    if request.method == "GET":
        players = Player_Details.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    ##This is for POST Request
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
##This function For PUT Request ***********

@csrf_exempt
def player_about(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        player = Player_Details.objects.get(player_id=id)
    except Player_Details.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = PlayerSerializer(player)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = PlayerSerializer(player, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        player.delete()
        return HttpResponse(status=204)


######################FROM now De-Serialization        ************************
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

##These 2 lines from app(team_players) and these two for both Seialization and DeSeialization
from team_players.models import Player_Details
from team_players.serializer import PlayerSerializer

@api_view(["GET", "POST"])
def players_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "GET":
        players = Player_Details.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
##This is for PUT Request
@api_view(["GET", "PUT", "DELETE"])
def players_about(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Player_Details.objects.get(player_id=id)
    except Player_Details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PlayerSerializer(snippet)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PlayerSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


########This is for class based