from django.forms import ModelForm 
from .models import Post
 
 
class PostForm(ModelForm):
 
    class Meta:
        model = Post
        fields = ['postAuthor', 'category_Type', 'postCategories', 'headline', 'main_part', 'rating'] 