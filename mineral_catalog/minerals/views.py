from django.shortcuts import render, get_object_or_404

from .models import Mineral


def show(request, object_id):
   object = Mineral.objects.filter(id=object_id).values()
   return render_to_response('minerals/mineral_detail.html', {'object': object})

def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})


def mineral_details(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/mineral_details.html', {'mineral': mineral})