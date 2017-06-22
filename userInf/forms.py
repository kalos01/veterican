#encoding:utf-8
from django  import forms
from datetime import datetime
from .models import Userinf
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
	password = forms.CharField(label=("Password"), widget=forms.PasswordInput)
	password2 = forms.CharField(label=("Password confirmation"), widget=forms.PasswordInput,
    							help_text=("Repita su password, por favor!"))
	date_joined = forms.DateTimeField(initial=datetime.now(),widget = forms.HiddenInput(), required = False)
	class Meta:
		model = Userinf
		fields = '__all__'

	def clean_email(self):
		email = self.cleaned_data.get("email")
		exists = User.objects.filter(email=email)
		if exists:
			raise forms.ValidationError("Ya existe un usuario con ese email.")
		return email

	def clean_password2(self):
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password != password2:
			raise forms.ValidationError("Las passwords no coinciden.")
		return password2

	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
		return user


"""	
	#self.user.set_password(self.cleaned_data['password'])
		if commit:
			self.user.save()
		return self.user
class UserFormTwo(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user"""