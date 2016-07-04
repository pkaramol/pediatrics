from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView, ListView,
CreateView, UpdateView, DeleteView)

from the_blog.models import BlogPost

from the_blog.forms import BlogPostForm


class HomeView(TemplateView):
    template_name = "home.html"
    # model = BlogPost

class AboutView(TemplateView):
    template_name = "about.html"


class BlogListView(ListView):
    template_name = "blog.html"
    model = BlogPost

class ContactView(TemplateView):
    template_name = "contact.html"

class BlogPostCreateView(CreateView):
    template_name = "blogpost-create.html"
    form_class = BlogPostForm

    def form_valid(self, form):
        """
        Assign the author to the request.user
        """
        form.instance.author = self.request.user
        return super(BlogPostCreateView, self).form_valid(form)

class BlogPostDetailView(DetailView):
    template_name = "blogpost-detail.html"
    model = BlogPost


# class BlogPostUpdateView(UpdateView):
#     template_name = "blogpost-update.html"
#     model = BlogPost
#     form_class = BlogPostForm
#
#
# class BlogPostDeleteView(DeleteView):
#     model = BlogPost
#     success_url = reverse_lazy('site-home')
