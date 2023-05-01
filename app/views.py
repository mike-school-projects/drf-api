from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Roster
from .serializer import RosterSerializer


class RosterList(ListAPIView):
    queryset = Roster.objects.all()
    serializer_class = RosterSerializer


class RosterDetail(RetrieveUpdateDestroyAPIView):
    queryset = Roster.objects.all()
    serializer_class = RosterSerializer