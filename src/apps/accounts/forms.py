from allauth.account.forms import SignupForm
from django import forms
from utils.choices import GENDER_CHOICES, UF_CHOICES, PROFILE_TYPE_CHOICES

import requests
def send_user_data_to_wix(user):
    wix_url = "https://marinahelou.com.br/_functions-dev/contact"
    wix_headers = {
        "Content-Type": "application/json"
    }
    wix_data = {
        "fullName": user.profile.full_name,
        "email": user.email,
        "phone" : user.profile.phone
    }

    try:
        response = requests.post(wix_url, headers=wix_headers, data=json.dumps(wix_data))
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        print("User data sent to Wix successfully.")

    except requests.exceptions.RequestException as e:
        print("Error sending user data to Wix:", e)


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

        send_user_data_to_wix(user)

        return user