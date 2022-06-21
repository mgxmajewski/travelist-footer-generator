from django import forms


class IdeaForm(forms.Form):
    user_idea = forms.CharField(label='Mamy taki pomysł, żeby...',
                                max_length=100,
                                widget=forms.Textarea(
                                    attrs={'placeholder': 'Poinformuj swoich partnerów o wymarzonym pomyśle wakacyjnym. '
                                                          'Dokończ powyższe zdanie i wygenerwuj plik do wstawienia '
                                                          'w stopkę maila.'}))
