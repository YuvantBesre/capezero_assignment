from rest_framework.generics import CreateAPIView, UpdateAPIView, GenericAPIView
from .serializers import ProjectSerializer, DealSerializer
from .models import Project, Deal
from rest_framework.response import Response
from rest_framework import status

class CreateProjectView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class CreateDealView(CreateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

class EditDealView(UpdateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

class GetTransferAmountView(GenericAPIView):

    def get(self, request, pk, format = None):
        response = Response(data = {}, status = status.HTTP_200_OK)

        try:
            deal = Deal.objects.prefetch_related('projects').get(id = pk)
            projects = deal.projects.all()

            data = {}
            total = 0

            for project in projects:
                tax_credit_transfer_amount = project.fmv * 0.3 * deal.tax_credit_transfer_rate
                data[project.name] = tax_credit_transfer_amount
                total += tax_credit_transfer_amount
            
            data['total'] = total
            response.data = data

            return response

        except Deal.DoesNotExist:
            response.data['message'] = 'Deal does not exist!'
            response.status_code = status.HTTP_400_BAD_REQUEST 

        return response