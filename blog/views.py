from pdb import post_mortem
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Post


class Postcreateview(CreateView):
    model = Post
    fields = "__all__"
    template_name = "Post_form.html"
    success_url = reverse_lazy("blog:all")
    
class Postlistview(ListView):
     model = Post 
     template_name = "Post_list.html"

class Postdetailview(DetailView):
    model = Post
    template_name = "Post_detail.html"
    
class Postupdateview(UpdateView):
    model = Post
    fields = "__all__"
    template_name = "Post_form.html"
    success_url = reverse_lazy("blog:all")

class Postdeleteview(DeleteView):
    model = Post
    fields = "__all__"
    template_name = "Post_confirm_delete.html"
    success_url = reverse_lazy("blog:all")