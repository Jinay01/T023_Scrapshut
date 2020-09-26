from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import RequirementsForm
# Create your views here.


def requirements(request):
    object_list = requirements.objects.all()
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'page': page, 'posts': posts}
    return render(request, 'main/user.html', context)


def ngo_summary(request, pk):
    context = {}
    return render(request, 'main/summary.html', context)


def ngo_tabular(request, pk):
    context = {}
    return render(request, 'main/tabular.html', context)


def ngo_requirementform(request, pk):
    ngo = Ngo.objects.get(user_id=pk)
    if request.method == "POST":
        form = RequirementsForm(request.POST)
        if form.is_valid:
            requirement = form.save(commit=False)
            requirement.ngo = ngo
            requirement.save()
            return redirect('main:tabular')
    else:
        form = RequirementsForm()
    context = {'form': form}
    return render(request, 'main/requirementform.html', context)
