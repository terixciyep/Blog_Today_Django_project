from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from feedback.forms import feedbackForm
import datetime


def feedbackPage(request):
    error = ''
    if request.method == 'POST':
        form = feedbackForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('MainPage:manpage'))
        else:
            error = form.errors
    else:
        form = feedbackForm(initial={'date_posted': datetime.datetime.today(), 'author': request.user})
    context = {
        'error':error,
        'form':form
    }
    return render(request, 'feedback/feedbackpage.html', context)