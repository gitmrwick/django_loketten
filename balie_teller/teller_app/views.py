from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Balie, Tel


def index(request):
    context = {'balie': Balie.objects.all(), }
    return render(request, 'teller_app/index.html', context)

@login_required
def admin(request):
    context = {'balie': Balie.objects.all(), }
    return render(request, 'teller_app/admin.html', context)

class BalieView(LoginRequiredMixin, generic.DetailView):
    model = Balie
    template_name = 'teller_app/balie.html'
    login_url = '/admin/'
    
    def post(self, request, *args, **kwargs):
        balie_id = kwargs['pk']
        balie = get_object_or_404(Balie, pk=balie_id)

        tel_master = Tel.objects.get(id=balie.tel_master.id)

        tel_master.tel_positie = F('tel_positie') + 1
        tel_master.save()

        tel_master = Tel.objects.get(id=balie.tel_master.id)
        tel_master.refresh_from_db()
        balie.balie_tel = tel_master.tel_positie
        balie.save()


        return HttpResponseRedirect(reverse('balie', args=(balie.id,)))
