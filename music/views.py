from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from music.models import Musician, Album
from music.serializers import MusicianSerializer, AlbumSerializer

class ListMusicians(APIView):
    """
    View to list all Musicians in the system.

    * Requires token authentication.
    """
    def get(self, request, format=None):
        """
        Return a list of all Musicians.
        """
        musicians = Musician.objects.all()
        serializer_musicians = MusicianSerializer(musicians, many=True)
        return Response(serializer_musicians.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer_musician = MusicianSerializer(data=request.data)
        if(serializer_musician.is_valid()):
            serializer_musician.save()
            return Response(serializer_musician.data, status=status.HTTP_201_CREATED)
        return Response(serializer_musician.data, status=status.HTTP_406_NOT_ACCEPTABLE)

class MusicianDetail(APIView):
    """
    View to list all Musicians in the system.

    * Requires token authentication.
    """

    def get_object(self, pk):
        try:
            return Musician.objects.get(pk=pk)
        except Musician.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        musician = self.get_object(pk)
        serializer_musician = MusicianSerializer(musician)
        return Response(serializer_musician.data)

    def put(self, request, pk, format=None):
        musician = self.get_object(pk)
        serializer_musician = MusicianSerializer(musician, data=request.data)
        if(serializer_musician.is_valid()):
            serializer_musician.save()
            return Response(serializer_musician.data, status=status.HTTP_200_OK)
        return Response(serializer_musician.data, status=status.HTTP_406_NOT_ACCEPTABLE)



