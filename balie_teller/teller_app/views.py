from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from .models import Balie


@login_required
def index(request):
    context = {'balie': Balie.objects.all(), }
    return render(request, 'teller_app/index.html', context)

@login_required
class BalieView(generic.DetailView):
    model = Balie
    template_name = 'teller_app/balie.html'
    
    def post(self, request, *args, **kwargs):
        print(f'post\n{args}\n{kwargs}\n{request}')
        balie_id = kwargs['pk']
        balie = get_object_or_404(Balie, pk=balie_id)

        balie.tel = balie.tel_master.tel_positie = F('tel_positie') + 1
        balie.save()

        return HttpResponseRedirect(reverse('balie', args=(balie.id,)))
