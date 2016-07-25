from django.core.urlresolvers import reverse_lazy
from django.views.generic import (TemplateView, DetailView, ListView,
CreateView, UpdateView, DeleteView)

from braces.views import SuperuserRequiredMixin

from the_blog.models import BlogPost

from the_blog.forms import BlogPostForm


class HomeView(SuperuserRequiredMixin, TemplateView):
    template_name = "home.html"
    # model = BlogPost

class AboutView(SuperuserRequiredMixin, TemplateView):
    template_name = "about.html"


class BlogListView(SuperuserRequiredMixin, ListView):
    template_name = "blog.html"
    model = BlogPost
    paginate_by = 4
    ordering = ["-created", "-updated"]

class ContactView(SuperuserRequiredMixin, TemplateView):
    template_name = "contact.html"


class BlogPostCreateView(SuperuserRequiredMixin, CreateView):
    template_name = "blogpost-create.html"
    form_class = BlogPostForm

    def form_valid(self, form):
        """
        Assign the author to the request.user
        """
        form.instance.author = self.request.user
        return super(BlogPostCreateView, self).form_valid(form)


class BlogPostDetailView(SuperuserRequiredMixin, DetailView):
    template_name = "blogpost-detail.html"
    model = BlogPost


class BlogPostUpdateView(SuperuserRequiredMixin, UpdateView):
    template_name = "blogpost-update.html"
    model = BlogPost
    form_class = BlogPostForm


class BlogPostDeleteView(SuperuserRequiredMixin, DeleteView):
    template_name = "blogpost_confirm_delete.html"
    model = BlogPost
    success_url = reverse_lazy('site-home')

# class Template404View(TemplateView):
#     template_name = "404.html"
#
# def handler404(request):
#     response = render_to_response('404.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 404
#     return response
