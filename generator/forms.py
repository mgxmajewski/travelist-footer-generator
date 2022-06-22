from django import forms


class IdeaForm(forms.Form):
    user_idea = forms.CharField(label='Mamy taki pomysł, żeby w wakacje',
                                max_length=100,
                                widget=forms.Textarea(
                                    attrs={'placeholder': 'nie wstawać z leżaka i liczyć gwiazdki hoteli.'}))
