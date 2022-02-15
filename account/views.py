from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView

from account.forms import ChangeBalanceUser
from account.models import CustomUser, SourcePoints


class AccountListView(ListView):
    model = CustomUser
    paginate_by = 10


class ChangeBalance(FormView):
    form_class = ChangeBalanceUser
    success_url = '/'
    template_name = 'account/customuser_form.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        try:
            CustomUser.objects.get(id=user_id)
        except (ValueError, CustomUser.DoesNotExist):
            raise Http404
        context = {'form': self.form_class(initial={'account': user_id}),
                   'user_id': user_id}
        return render(request, self.template_name, context)


class SourcePointsView(CreateView):
    model = SourcePoints
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy('change-balance',
                            kwargs={'user_id': self.kwargs.get('user_id')})
