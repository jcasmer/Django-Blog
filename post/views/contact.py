from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from django.contrib import messages

from post.models import ContactRequest
from post.forms import ContactRequestForm

from libraries.utilities import Utilites


class ContactView(View):

    template_name = 'contact/contact.html'

    def get(self, request, *args, **kwargs):

        form = ContactRequestForm()
        output = {
            'form': form,
        }
        return render(request, self.template_name, output)

    def post(self, request, *args, **kwargs):

        form = ContactRequestForm(request.POST)
        output = {
                'form': form,
            }
        if not form.is_valid():
            messages.error(request, 'see errors')
            
            return render(request, self.template_name, output)       
        
        err = Utilites.send_email(form.cleaned_data)
        if err:
            messages.error(request, err)
            return render(request, self.template_name, output)
        
        form.save()
        messages.success(request, 'Contact sent successfully')        
        return HttpResponseRedirect(reverse('post:index'))