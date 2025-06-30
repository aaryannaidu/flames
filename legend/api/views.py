from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from legend.models import FlamesResult
from .serializers import FlamesResultSerializer, FlamesCalculateSerializer

class FlamesResultViewSet(viewsets.ModelViewSet):
    queryset = FlamesResult.objects.all()
    serializer_class = FlamesResultSerializer

@api_view(['POST'])
def calculate_flames(request):
    serializer = FlamesCalculateSerializer(data=request.data)
    if serializer.is_valid():
        name1 = serializer.validated_data['name1'].lower().replace(" ", "")
        name2 = serializer.validated_data['name2'].lower().replace(" ", "")
        
        # FLAMES calculation logic
        for letter in name1:
            if letter in name2:
                name1 = name1.replace(letter, "", 1)
                name2 = name2.replace(letter, "", 1)
        
        count = len(name1) + len(name2)
        flames = ["Friends👀", "Love😍", "Affection😌", "Marriage💍", "Enemy😠", "Sibling 😵‍💫"]
        
        while len(flames) > 1:
            i = (count - 1) % len(flames)
            flames.pop(i)
        
        result = flames[0]
        
        # Save to database
        flames_result = FlamesResult.objects.create(
            name1=serializer.validated_data['name1'],
            name2=serializer.validated_data['name2'],
            result=result
        )
        
        # Return the result
        result_serializer = FlamesResultSerializer(flames_result)
        return Response(result_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_results_history(request):
    results = FlamesResult.objects.all().order_by('-id')[:10]  # Get the latest 10 results
    serializer = FlamesResultSerializer(results, many=True)
    return Response(serializer.data)
