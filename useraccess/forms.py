from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomRegisterFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']
        # fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'form-control'})