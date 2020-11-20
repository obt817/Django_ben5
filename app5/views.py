from django .views.generic import TemplateView


class indexView(TemplateView):
    template_name = 'index.html'


class aboutView(TemplateView):
    template_name = 'about.html'
