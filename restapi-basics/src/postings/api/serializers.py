from rest_framework import serializers

from postings.models import BlogPost

#creating a serializer
class BlogPostSerializer(serializers.ModelSerializer):
    url   = serializers.SerializerMethodField(read_only=True)
    class Meta:
       model = BlogPost
       fields = [
         'url',
	     'pk',
		 'user',
		 'title',
		 'content',
		 'timestamp',
]
    read_only_fields = ['user']


    def get_url(self, obj):
       request = self.context.get("request")
       return obj.get_api_url(request=request)

    def validate_title(self, value):
        qs = BlogPost.objects.filter(title_iexact=value)
        if self.instance:
          qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
          raise serializers.ValidateError("This title has already been used.")
        return value









