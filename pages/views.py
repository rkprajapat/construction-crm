from django.views.generic import TemplateView

from projects.models import Project


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['project_list'] = Project.objects.all()
        return context


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'