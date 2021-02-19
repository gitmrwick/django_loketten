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

        balie_groep = Balie.objects.filter(balie_groep__exact=balie.balie_groep)
        balie_groep_tels = [b.balie_tel for b in balie_groep]

        balie_tel_master = balie.tel_master
        balie_tel_master_positie = balie_tel_master.tel_positie

        balie.balie_tel = F('balie_tel') + 1
        balie.save()
        return HttpResponseRedirect(reverse('balie', args=(balie.id,)))
