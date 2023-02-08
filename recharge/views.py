from .serializers import PlaneSerializer
from rest_framework import generics
from .models import Planes
# Create your views here.

class PlanListView(generics.ListAPIView):
    
    queryset = Planes.objects.all()
    serializer_class = PlaneSerializer
    
    