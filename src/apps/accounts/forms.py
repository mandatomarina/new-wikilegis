from allauth.account.forms import SignupForm
from django import forms
from utils.choices import GENDER_CHOICES, UF_CHOICES, PROFILE_TYPE_CHOICES


class CustomSignupForm(SignupForm):

    full_name = forms.CharField(label="Nome Completo", max_length=200)
    uf = forms.ChoiceField(choices=UF_CHOICES, label='Estado')
    elector = forms.BooleanField(label="É eleitor(a) da Marina?", required=False)
    phone = forms.CharField(label="Celular", max_length=20)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        up = user.profile
        up.full_name = self.cleaned_data['full_name']
        up.uf = self.cleaned_data['uf']
        up.phone = self.cleaned_data['phone']
        up.elector = self.cleaned_data['elector']
        up.save()
        return user
