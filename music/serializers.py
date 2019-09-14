from rest_framework import serializers
from music.models import Musician, Album

class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = '__all__'

    def create(self, validated_data):
        return Musician.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.instrument = validated_data.get('instrument', instance.instrument)
        instance.save()
        return instance

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'