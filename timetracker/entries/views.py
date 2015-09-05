from django.utils import timezone
from django.core.urlresolvers import reverse_lazy

from django.views.generic import UpdateView, CreateView

from .forms import EntryForm, ProjectForm, ClientForm
from .models import Client, Entry, Project


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    context_object_name = 'client'
    template_name = 'clients.html'
    success_url = reverse_lazy('client-list')

    def get_context_data(self, **kwargs):
        context = super(ClientCreateView, self).get_context_data(**kwargs)
        context['clients'] = Client.objects.all()

        return context

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_detail.html'
    success_url = reverse_lazy('client-list')


class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm
    context_object_name = 'entry'
    template_name = 'entries.html'
    success_url = reverse_lazy('entry-list')

    def get_form_kwargs(self):
        kwargs = super(EntryCreateView, self).get_form_kwargs()
        # Does user want stop field filled in with current time?
        if self.request.method == 'POST' and 'alt_submit' in self.request.POST:
            # Yes
            kwargs['data'] = kwargs['data'].copy()
            kwargs['data']['stop'] = timezone.now()

        return kwargs

    def form_invalid(self, form):
        # If the form is invalid and user pressed the button
        # to fill stop in with the current time, unfill it before
-       # redisplaying.
        if self.request.method == "POST" and 'alt_submit' in self.request.POST:
            form.data['stop'] = ""
        return super(EntryCreateView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(EntryCreateView, self).get_context_data(**kwargs)
        context['entries'] = Entry.objects.all()

        return context


class EntryUpdateView(UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'entry_detail.html'
    success_url = reverse_lazy('entry-list')


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    context_object_name = 'project'
    template_name = 'projects.html'
    success_url = reverse_lazy('project-list')

    def get_context_data(self, **kwargs):
        context = super(ProjectCreateView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()

        return context


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_detail.html'
    success_url = reverse_lazy('project-list')
