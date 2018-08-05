# generic views
from django.db.models import Q
from rest_framework import generics, mixins
from postings.models import BlogPost
from .permissions import IsOwnerOrReadOnly
from .serializers import BlogPostSerializer

class BlogPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field         = 'pk' # use slug / id   # url(?P<pk>d+)
    serializer_class     = BlogPostSerializer

    def get_queryset(self):
        qs = BlogPost.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
          qs = qs.filter(Q(title_icontains=query)|Q(title_icontains=query))
        return BlogPost.objects.all()
	   
    def perform_create(self, serializer):
	    serializer.save(user=self.request.user)
		
    def post(self, request, *args, **kwargs):
	    return self.create(request, *args,  **kwargs)
		
    def put(self, request, *args, **kwargs):
	    return self.update(request, *args,  **kwargs)
		
    def patch(self, request, *args, **kwargs):
	    return self.update(request, *args,  **kwargs)
 
class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView): # detailview
    lookup_field         = 'pk' # use slug / id   # url(?P<pk>d+)
    serializer_class     = BlogPostSerializer
    permission_classes   = [IsOwnerOrReadOnly]
    #queryset             = BlogPost.objects.all()
	 
    def get_queryset(self):
       return BlogPost.objects.all()

     #def get_object(self):
     #   pk = self.kwargs.get("pk")
     #   return BlogPost.objects.all()	 
	 
    def validate_title(self, value):
      qs = BlogPost.objects.filter(title_iexact=value) 
      if self.instance:  
        qs = qs.exclude(pk=self.instance.pk)  
      if qs.exists():  
        raise serializers.ValidationError("The title must be unique")   
      return value
		
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 