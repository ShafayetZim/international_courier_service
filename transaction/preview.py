from django.http import HttpResponseRedirect

from formtools.preview import FormPreview
from .models import Transaction


class TransactionFormPreview(FormPreview):
    preview_name = 'form.html'

    def done(self, request, cleaned_data):
        # Do something with the cleaned_data, then redirect
        # to a "success" page.
        return HttpResponseRedirect('/form/success')