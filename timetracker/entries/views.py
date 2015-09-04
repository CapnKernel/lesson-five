from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import EntryForm, ProjectForm, ClientForm
from .models import Client, Entry, Project


def clients(request):
    if request.method == 'POST':
        # Create our form object with our POST data
        form = ClientForm(request.POST)
        if form.is_valid():
            # If the form is valid, create a client with submitted data
            form.save()
            return redirect('client-list')
    else:
        form = ClientForm()

    client_list = Client.objects.all()
    return render(request, 'clients.html', {
        'client_list': client_list,
        'form': form,
    })


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            # Update client details
            form.save()
            return redirect('client-list')
    else:
        # Initialise form with client data
        form = ClientForm(instance=client)

    return render(request, 'client_detail.html', {
        'client': client,
        'form': form,
    })


def entries(request):
    if request.method == 'POST':
        # Create our form object with our POST data
        # We use .copy() so the dict the form uses for storing field
        # data is mutable.
        entry_form = EntryForm(request.POST.copy())
        # Does user want stop field filled in with current time?
        if 'alt_submit' in request.POST:
            entry_form.data['stop'] = timezone.now()
        if entry_form.is_valid():
            # If the form is valid, let's create an Entry with the submitted data
            entry_form.save()
            return redirect('entry-list')
        else:
            if 'alt_submit' in request.POST:
                # If the form is invalid and user pressed the button
                # to fill stop in with the current time, unfill it before
                # redisplaying.
                entry_form.data['stop'] = ""

    else:
        entry_form = EntryForm()

    entry_list = Entry.objects.all()
    return render(request, 'entries.html', {
        'entry_list': entry_list,
        'form': entry_form,
    })


def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)

    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            # Update entry details
            form.save()
            return redirect('entry-list')
    else:
        # Initialise form with entry data
        form = EntryForm(instance=entry)

    return render(request, 'entry_detail.html', {
        'entry': entry,
        'form': form,
    })


def projects(request):
    if request.method == 'POST':
        # Create our form object with our POST data
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project-list')
    else:
        form = ProjectForm()

    project_list = Project.objects.all()
    return render(request, 'projects.html', {
        'project_list': project_list,
        'form': form
    })


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            # Update project details
            form.save()
            return redirect('project-list')
    else:
        # Initialise form with project data
        form = ProjectForm(instance=project)

    return render(request, 'project_detail.html', {
        'project': project,
        'form': form,
    })
