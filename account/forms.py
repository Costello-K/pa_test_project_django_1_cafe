from django import forms
from django.contrib.auth import get_user_model, authenticate


class LoginForm(forms.Form):

    class Meta:
        model = get_user_model()
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
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'phone', 'email', )

    username = forms.CharField(widget=forms.TextInput(attrs={
                                'type': "text",
                                'class': "form-control",
                                'placeholder': "Введіть унікальне ім'я для сайту username"})
                               )
    first_name = forms.CharField(widget=forms.TextInput(attrs={
                                'type': "text",
                                'class': "form-control",
                                'placeholder': "Ім'я"})
                                 )
    last_name = forms.CharField(widget=forms.TextInput(attrs={
                                'type': "text",
                                'class': "form-control",
                                'placeholder': "Прізвище"})
                                )
    phone = forms.CharField(widget=forms.TextInput(attrs={
                                'type': "text",
                                'class': "form-control",
                                'placeholder': "Номер телефону"})
                            )
    email = forms.CharField(widget=forms.TextInput(attrs={
                                'type': "text",
                                'class': "form-control",
                                'placeholder': "e-mail"})
                                   )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                'type': "password",
                                'class': "form-control",
                                'placeholder': "Пароль"})
                               )
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
                                'type': "password",
                                'class': "form-control",
                                'placeholder': "Повторіть пароль"})
                                )

    def clean_password2(self):
        if self.cleaned_data['password'] == self.cleaned_data['confirm_password']:
            return self.cleaned_data['password']
        raise forms.ValidationError('Паролі не співпадають')
