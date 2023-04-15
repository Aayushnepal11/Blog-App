from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import BlogPost
from .forms import CreatePost
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import Http404


class HomePageView(ListView):
    template_name = "index.html"
    model = BlogPost
    context_object_name = "blogs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_data"] = self.model.objects.filter(owner=self.request.user.id).order_by('date_added')
        return context
    


class BlogDetailView(DetailView):
    template_name = "details.html"
    def get(self, request,pk):
        blog_text = get_object_or_404(BlogPost, id=pk)
        blog_text_data = blog_text.text
        num_visit = request.session.get('num_visit', 0)
        request.session['num_visit'] = num_visit + 1
        
        if request.user.is_authenticated and blog_text.owner != request.user:
            raise Http404

        context = {
            'title': f"BlogDetails/{BlogPost.objects.get(id=pk).title}",
            'id': blog_text,
            'blog_text': blog_text_data,
            'num_visit': num_visit
        }
        return render(request,self.template_name, context)

@method_decorator(login_required, name="dispatch")
class CreateBlogPostView(CreateView):
    model = BlogPost
    template_name = "create_post.html"
    form_class = CreatePost

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

@method_decorator(login_required, name="dispatch")
class EditBlogPostView(UpdateView):
    template_name = "edit_post.html"
    form_class = CreatePost
    queryset = BlogPost.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(BlogPost, id=id_)

    def form_valid(self, form):
        if BlogPost.objects.filter(owner=self.request.user):
            form.save()
        else:
            raise Http404
        return super().form_valid(form)
    
    def get_success_url(self):
        return "/"

