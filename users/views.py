from django.views.generic import CreateView
from .forms import CustomUserCreation
from django.shortcuts import redirect, render
from django.contrib.auth import login

class RegisterViewPage(CreateView):
    template_name = "registration/register.html"
    form_class = CustomUserCreation
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email = form.cleaned_data.get('email')
            user.email = email
            user.save()
            login(request,user)
            return redirect("blogs:home")
        return super().post(request, self.template_name, {'form': form})
    

    

