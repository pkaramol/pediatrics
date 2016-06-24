from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView, ListView,
CreateView, UpdateView, DeleteView)

from the_blog.models import BlogPost

from the_blog.forms import BlogPostForm


class BlogHomeView(TemplateView):
    template_name = "index.html"
    # model = BlogPost

    def get_context_data(self, **kwargs):
        context = super(BlogHomeView, self).get_context_data(**kwargs)
        context["title"] = "Πάμε μωρή Πανάθα!"
        return context


class BlogPostDetailView(DetailView):
    template_name = "blogpost-detail.html"
    model = BlogPost


class BlogHomeListView(ListView):
    template_name = "blogpost-list.html"
    model = BlogPost


class BlogPostCreateView(CreateView):
    template_name = "blogpost-create.html"
    form_class = BlogPostForm

    def form_valid(self, form):
        """
        Assign the author to the request.user
        """
        form.instance.author = self.request.user
        return super(BlogPostCreateView, self).form_valid(form)


class BlogPostUpdateView(UpdateView):
    template_name = "blogpost-update.html"
    model = BlogPost
    form_class = BlogPostForm


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('site-home')
