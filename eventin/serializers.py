from rest_framework import serializers
from .models import Evento, Participante, Inscricao

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__' #['campo a', 'campo b', 'campo c']

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = '__all__'

class InscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields = '__all__'

class ListaInscricoesParticipanteSerializer(serializers.ModelSerializer):
    evento = serializers.ReadOnlyField(source='evento.nome')
    class Meta:
        model = Inscricao
        fields = ["evento", "data_inscricao"]

class ListaInscricoesEventoSerializer(serializers.ModelSerializer):
    participante = serializers.ReadOnlyField(source='participante.nome')
    class Meta:
        model = Inscricao
        fields = ["participante", "data_inscricao"]