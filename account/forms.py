from django import forms

from account.models import Transaction


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.name}"


class ChangeBalanceUser(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = {
            'account': forms.HiddenInput()
        }
        help_texts = {
            'value': ('If you want remove points please put "-" before value'),
        }
        field_classes = {
            'source_type': MyModelChoiceField,
        }

    def save(self):
        data = self.cleaned_data
        user = data.get('account')
        user.balance += data.get('value')
        user.save()
        transaction = super(ChangeBalanceUser, self).save(commit=True)
        return transaction
