from django.contrib.auth.forms import UserCreationForm


class UserCreateFrom(UserCreationForm):
    def __init__(self, *args, **kwargs) -> None:
        super(UserCreationForm,self).__init__(*args, **kwargs)

        for fieldname in ['username','password1','password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})      