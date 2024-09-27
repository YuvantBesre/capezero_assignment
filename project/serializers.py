from rest_framework import serializers
from .models import Deal, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class DealSerializer(serializers.ModelSerializer):
    project_details = ProjectSerializer(read_only = True, many = True, source = 'projects')
    
    def validate(self, attrs):
        if attrs.get('tax_credit_transfer_rate', None):
            if attrs['tax_credit_transfer_rate'] < 0 or attrs['tax_credit_transfer_rate'] > 1:
                raise serializers.ValidationError('Invalid value for Tax Credit Transfer rate! Should be 0-1')
        return attrs

    class Meta:
        model = Deal
        fields = '__all__'
        extra_kwargs = {
            'projects' : { 'write_only' : True }
        }