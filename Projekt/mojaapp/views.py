
from django.shortcuts import render, redirect
from .forms import UstawieniaForm

def zmien_ustawienia(request):
    if request.method == 'POST':
        form = UstawieniaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Przekieruj do strony głównej po zapisaniu
    else:
        form = UstawieniaForm()
    return render(request, 'nazwa_aplikacji/ustawienia.html', {'form': form})
