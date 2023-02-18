from django.shortcuts import redirect, render
from django.utils.timezone import datetime
from django.views.generic import ListView

from hello.forms import LogMessageForm
from hello.models import LogMessage


class HomeListView(ListView):
    model = LogMessage
    template_name = 'hello/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def log_message(request):   # pylint: disable=R1710
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect('home')
    else:
        return render(
            request,
            'hello/log_message.html',
            {
                'form': form,
            }
        )

def about(request):
    return render(request, 'hello/about.html')

def contact(request):
    return render(request, 'hello/contact.html')
