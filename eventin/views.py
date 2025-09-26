from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Evento, Participante, Inscricao
from .serializers import (EventoSerializer, ParticipanteSerializer, InscricaoSerializer,
                          ListaInscricoesParticipanteSerializer, ListaInscricoesParticipanteSerializer,
                          ListaInscricoesEventoSerializer)

class EventoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated] # Qualquer usuário cadastrado
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class ParticipanteViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated] # Qualquer usuário cadastrado
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer

class InscricaoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser] # Somente usuário Admin
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer

class ListaInscricoesParticipante(generics.ListAPIView):
    serializer_class = ListaInscricoesParticipanteSerializer

    def get_queryset(self):
        participante_id = self.kwargs["pk"]
        return Inscricao.objects.filter(participante_id=participante_id)

class ListaInscricoesEvento(generics.ListAPIView):
    serializer_class = ListaInscricoesEventoSerializer

    def get_queryset(self):
        evento_id = self.kwargs["pk"]
        return Inscricao.objects.filter(evento_id=evento_id)