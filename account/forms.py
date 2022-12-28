from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class LoginForm(forms.Form):

    class Meta:
        model = User
        fields = ('username', )

    username = forms.CharField(widget=forms.TextInput(attrs={
                                'type': "text",
                                'class': "form-control",
                                'placeholder': "username"})
                               )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                'type': "password",
                                'class': "form-control",
                                'placeholder': "Пароль"})
                               )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                raise forms.ValidationError('Не вірний логін або пароль')
        return super().clean()


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname', 'phone', )

    username = forms.CharField(widget=forms.TextInput(attrs={
                                'type': "text",
                                'class': "form-control",
                                'placeholder': "username"})
                               )
    firstname = forms.CharField(widget=forms.TextInput(attrs={
                                'type': "text",
                                'class': "form-control",
                                'placeholder': "Ім'я"})
                                )
    lastname = forms.CharField(widget=forms.TextInput(attrs={
                                'type': "text",
                                'class': "form-control",
                                'placeholder': "Фамілія"})
                               )
    phone = forms.CharField(widget=forms.TextInput(attrs={
                                'type': "text",
                                'class': "form-control",
                                'placeholder': "Номер телефону"})
                            )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                'type': "password",
                                'class': "form-control",
                                'placeholder': "Пароль"})
                               )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                                'type': "password",
                                'class': "form-control",
                                'placeholder': "Повторіть пароль"})
                                )

    def clean_password2(self):
        if self.cleaned_data['password'] == self.cleaned_data['password2']:
            return self.cleaned_data['password']
        raise forms.ValidationError('Паролі не співпадають')
