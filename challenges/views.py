import subprocess
from .models import Challenge
from .serializers import ChallengeSerializer, ChallengeDetailSerializer, CodeTestSerializer
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ChallengePagination(PageNumberPagination):    
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class ChallengeListCreateView(generics.ListCreateAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    pagination_class = ChallengePagination
    permission_classes = [permissions.IsAuthenticated]  


class ChallengeDetailView(generics.RetrieveAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeDetailSerializer
    permission_classes = [permissions.IsAuthenticated]  





class CodeTestView(APIView):
    def post(self, request):
        serializer = CodeTestSerializer(data=request.data)
        if serializer.is_valid():
            test_code = serializer.validated_data['test']
            solution_code = serializer.validated_data['solution']

            
            with open("code_to_test.py", "w", encoding="utf-8") as f:
                f.write("# -*- coding: utf-8 -*-\n")
                f.write(solution_code + "\n\n")  
                f.write(test_code) 
                print("guarde el codigo en un archivo temporal")

                
            # Imprimir el contenido del archivo para verificar
            # with open("code_to_test.py", "r") as f:
            #     print("Contenido de code_to_test.py:")
            #     print(f.read())
                
            try:
                
                result = subprocess.run(
                ["python", "code_to_test.py"],  
                capture_output=True,
                text=True,
                )

                output = result.stdout if result.returncode == 0 else result.stderr
                print("Resultado del código:", output)

                return Response(
                    {"result": "success" if result.returncode == 0 else "failure", "output": output},
                    status=status.HTTP_200_OK
                )

            except Exception as e:
                return Response(
                    {"result": "error", "error": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
