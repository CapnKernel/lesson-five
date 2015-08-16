## MelbDjango School - Lesson Five

Class Based Views & ModelForms

---

## WIFI

Common Code / cc&20!4@

---

## A brief look at OO

- Object Oriented Programming
- Software development methodology
- A way to describe data and its interactions in code
- Objects are things - Any-things
- Concept first goes back to the 60s
- Popularised by the Smalltalk language in the early 1980s
- Became a dominant programming methodology with the introduction of C++, Visual FoxPro and Delphi
- Python, Java, Javascript, Ruby, Perl, Lisp (to name a few) - All incorporate OO concepts

---

## Classes

- A Class defines an object
- What sort of object? - Anything!

---

## A Car

![](http://www.wellclean.com/wp-content/themes/artgallery_3.0/images/car3.png)

---

## A Person

![](http://vignette2.wikia.nocookie.net/kimpossible/images/8/86/Placeholder_person.png)

---

## A Car Person

![](http://beakerhead.com/wp-content/uploads/2014/04/art-car-parade.jpg)

---

## Properties of Python classes

- Attributes
- Methods
- Bases (For managing inheritance)

---

## Attributes

- Describe the object
  - Car - Engine, Wheels, Seats, Doors...
  - Person - Head, Eyes, Arms, Legs...

---

## Methods

- Describe what the object can do
  - Car - Drive, Turn, Stop
  - Person - Walk, Run, Talk

---

## Classes in Python

- Define a basic Vehicle
  - Attributes: Engine, Wheels
  - Methods: Drive, Stop

```
class DefaultVehicle:
    engine = '4 Cylinder'
    wheels = 4

    def drive(self):
        pass

    def stop(self):
        pass
```

---

## Inheritance

- Define a Tank using our DefaultVehicle class as a base

![](http://www.incredible-adventures.com/tanks/drive-tank-001.jpg)

---

## Tank Class

- In addition to DefaultVehicle a tank has a turret and can shoot
- Engine and wheels values are also different

  ```
  class Tank(DefaultVehicle):
      engine = 'Massive' # Try googling for "tank engine"
      wheels = 20
      turret = 'Large calibre'

      def shoot(self):
          pass
  ```

- Tank __overloaded__ the engine and wheels with its own values
- Tank still has drive and stop capabilities as they are implied by inheriting from the parent class DefaultVehicle

  ```
  tank = Tank()
  tank.drive() # From parent (super) class DefaultVehicle
  tank.stop()  # From parent (super) class DefaultVehicle
  tank.shoot()
  ```


---

## Another class example

### Person

```
class Person:
    head = 'large'
    eyes = 2
    arms = 2
    legs = 2

    def walk(self):
        pass

    def run(self):
        pass

    def talk(self):
        pass
```

---

## Mix it up

### What sort of object will this code produce?

  ```
  class VehiclePerson(DefaultVehicle, Person):
      pass
  ```

- Remember that the attributes and methods of both __superclasses__ are implied by this definition
- Attributes and methods can be overloaded in this new class just like any other

---

### Something like this?

![](http://beakerhead.com/wp-content/uploads/2014/04/art-car-parade.jpg)

---

## I have created a monster!

  ```
  freak_of_nature = VehiclePerson()
  freak_of_nature.drive()
  freak_of_nature.walk()
  freak_of_nature.run()
  freak_of_nature.stop()
  freak_of_nature.talk()
  ```

---

## OO Jargon

### Inheritance

- Objects inherit everything from their parent (super) class
- Tank inherited wheels, engine, drive() and stop() from DefaultVehicle
- Eliminates repetition

---

## OO Jargon

### Multiple Inheritance (Mixins)

- VehiclePerson class is a combination of DefaultVehicle and Person

---

## OO Jargon

### Overloading

- Tank replaces its superclass' attributes "wheels" and "engine" with its own values

---

## OO Jargon

### Polymorphism

- Different behaviour depending on the type of object the code is interacting with
- Out of scope for this presentation
- Python implements its own take on this concept

---

## Class Based Views

- Drop in replacement for function based views
- Allows all of that cool OO stuff. Inheritance etc
- Implement sensible defaults
- Less coding, more getting stuff done. __DRY__

---

## Django Builtins

- Generic Class Based Views
- Commonly used generic view classes
  - TemplateView
  - DetailView
  - ListView
  - CreateView
  - UpdateView
  - DeleteView
  - RedirectView

---

## TemplateView

- Basic page functionality

```
from django.views.generic import TemplateView

class MyTemplateView(TemplateView):
    template_name = 'my_template.html'
```

- urls.py

``url(r'^$', TemplateView.as_view(), name='root')``

---

## DetailView

- Display information about a single model instance

```
from django.views.generic import DetailView

class MyModelDetailView(DetailView):
    model = MyModel # All that is required!
    # Omit the below attribute and django will default to the
    # template name 'mymodel_detail.html'
    template_name = 'my_detail_template.html'
    # Below is default - but you can change this too!
    template_name_suffix = '_detail'
    pk_url_kwarg = 'pk' # Also default. Here for explicitness
    context_object_name = 'my_object' # Default is "object"
```

- urls.py

``
url(r'^my-models/(?P<pk>\d+)/$', MyModelDetailView.as_view(), name='my-model-detail')
``

---

## ListView

- Display a list of instances of a particular model

```
from django.views.generic import ListView

class MyModelListView(ListView):
    model = MyModel # All that is required!
    template_name_suffix = '_list' # Default
    context_object_name = 'my_object' # Default is "object"
```

- urls.py

``
url(r'^my-models/$', MyModelListView.as_view(), name='my-model-list')
``

---

## CreateView

- Generate a single model instance from a form

```
from django.views.generic import CreateView

class MyModelCreateView(CreateView):
    model = MyModel
    form_class = MyModelForm
    success_url = '/'
    # That's it!
```

- urls.py

``
url(r'^my-models/create/$', MyModelCreateView.as_view(), name='my-model-create')
``

---

## UpdateView

- Update a single model instance with a form

```
from django.views.generic import UpdateView

class MyModelUpdateView(UpdateView):
    model = MyModel
    form_class = MyModelForm
    success_url = '/'
    # That's it!
```

- urls.py

``
url(r'^my-models/(?P<pk>\d+)/update/$', MyModelUpdateView.as_view(), name='my-model-update')
``

---

## DeleteView

- Delete a single model instance

```
from django.views.generic import DeleteView

class MyModelDeleteView(DeleteView):
    model = MyModel
    success_url = '/'
    # That's it!
```

- urls.py

``
url(r'^my-models/(?P<pk>\d+)/delete/$', MyModelDeleteView.as_view(), name='my-model-delete')
``

---

## FormView

- Display a template with a form

```
from django.views.generic import FormView

class MyFormView(FormView):
    form_class = MyForm
    success_url = '/'
    template_name = 'my_template.html'
    # That's it!
```

- urls.py

``
url(r'^form/$', MyFormView.as_view(), name='a-form')
``

---

## Generic Views

- And much more...

---

## Last week's example

```
def django_example(request):
    if request.method == 'POST':
        form = HelloWorldForm(request.POST)
        if form.is_valid():
            return render(request, 'django_form.html', {
                'form': form,
                'name': form.cleaned_data['name']
            })
    else:
        form = HelloWorldForm()

    return render(request, 'django_form.html', {
        'form': form,
    })
```

### Drawbacks

- Form doesn't generate any data
- How to generate instances of this model?

```
class Person(models.Model):
    name = models.CharField(max_length=30)
    awesome = models.BooleanField()
```


---

## Improvements

- We could modify similar to last week's work

```
def person_create(request):
    if request.method == 'POST':
        form = HelloWorldForm(request.POST)
        if form.is_valid():
            # Create person instance
            person = Person()
            person.name = form.cleaned_data['name']
            person.awesome = form.cleaned_data['awesome']
            person.save()
            return render(request, 'django_form.html', {
                'form': form,
                'name': person.name
            })
    else:
        form = HelloWorldForm()

    return render(request, 'django_form.html', {
        'form': form,
    })
```

- Or ???

---

## Generic class based view implementation

```
from django.views.generic import CreateView
from django.core.urlresolvers import reverse

class PersonCreateView(CreateView):
    """
    View to create a Person instance every time the form is submitted
    """
    model = Person
    template_name = 'django_form.html'
    form_class = HelloWorldForm
    context_object_name = 'person' # "object" is the default

    def get_context_data(self, **kwargs):
        context = super(PersonCreateView, self).get_context_data(**kwargs)
        context['name'] = self.person.name
        return context

    def get_success_url(self):
        """
        Just redirect to the same page if the form is valid
        """
        return reverse('django_form')
```

---

## Last week's form

```
from django import forms

class HelloWorldForm(forms.Form):
    name = forms.CharField(required=True, label="Say Hello")
    awesome = forms.BooleanField(label="Are they awesome?")

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.lower().startswith('b'):
            raise forms.ValidationError("Wait a second, your name doesn't start with B!")
        return name
```

- Describes fields on our Person model
- Explicit

---

## ModelForm Equivalent

```
from django import forms
from .models import Person

class HelloWorldForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'awesome')
        labels = {
            'name': 'Say Hello',
            'awesome': 'Are they awesome?'
        }
        # widgets = {}

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.lower().startswith('b'):
            raise forms.ValidationError("Wait a second, your name doesn't start with B!")
        return name
```

---

## Wait - what was that Meta thing again?

- A kind of "settings" or "config" for many django class types
- Used on models too!

  ```
  class Person(models.Model):
      class Meta:
          verbose_name_plural = 'People'
          
      name = models.CharField(max_length=30)
      awesome = models.BooleanField()

      def __str__(self):
          return '{} ({})'.format(self.name, 'Totally Awesome' if self.awesome else 'Lame')
  ```

- Check django docs for uses

---

## Homework

- Last week's solution in lesson-five repo (bootstrappy)

### This week's homework

- Fork https://github.com/MelbDjango/lesson-five
- Clone the repo to your own machine
- Use the virtualenv you created in previous lesson
- Convert time-tracker forms and views to ModelForms and Generic Class Based Views
- Bonus 1: Create a RedirectView to redirect visitors from the root of the site (/) to the /clients/ page
- Bonus 2: Add a button to the "entries" form (/entries/) called "Create Entry with End Now"
  - This button should be an alternative submit button that automatically sets the end time to be the current time

---

## References

- https://ccbv.co.uk/
- REFERENCES.md in lesson-five repo
- Check out formexample

