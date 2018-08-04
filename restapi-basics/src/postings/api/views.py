# generic views

from rest_framework import generics
from postings.models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView): # detailview
     lookup_field         = 'pk' # use slug / id   # url(?P<pk>d+)
     serializer_class     = BlogPostSerializer
     #queryset             = BlogPost.objects.all()
	 
     def get_queryset(self):
        return BlogPost.objects.all()

     #def get_object(self):
     #   pk = self.kwargs.get("pk")
     #   return BlogPost.objects.all()	 
	 
	 