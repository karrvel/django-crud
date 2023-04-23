from django.shortcuts import get_object_or_404, redirect, render
from accounts import models, forms
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login')
def customuser(request):
    if 'q' in request.GET:
        q = request.GET['q']
        users = models.CustomUser.objects.filter(username__icontains = q)
    else:
        users = models.CustomUser.objects.all().order_by('-id')

    counts = users.count()
    erkak = models.CustomUser.objects.filter(gender = 'Erkak').count()
    ayol = models.CustomUser.objects.filter(gender = 'Ayol').count()

    context = {
        'users' : users,
        'counts' : counts,
        'erkak' : erkak,
        'ayol' : ayol
    }

    return render(request, 'index.html', context)


@login_required(login_url='/login')
def delete(request, pk):
    user = get_object_or_404(models.CustomUser, pk=pk)
    user.delete()
    return redirect('home')

@login_required(login_url='/login')
def edit(request, pk):
    user = get_object_or_404(models.CustomUser, pk=pk)
    if request.method == 'POST':
        form = forms.CustomUserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.CustomUserUpdateForm(instance=user)
    
    return render(request, 'edit.html', {'user': user, 'form': form})