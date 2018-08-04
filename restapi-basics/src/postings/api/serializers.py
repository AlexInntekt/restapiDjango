from rest_framework import serializers

from postings.models import BlogPost

#creating a serializer
class BlogPostSerializer(serializers.ModelSerializer):
     class Meta:
       model = BlogPost
       fields = [
	     'pk',
		 'user',
		 'title',
		 'content',
		 'timestamp',
		 
]














