from django import forms


class IdeaForm(forms.Form):
    your_name = forms.CharField(label='Mamy taki pomysł, żeby...',
                                max_length=100,
                                widget=forms.TextInput(
                                    attrs={'class': 'myfieldclass',
                                           'placeholder': 'Poinformuj swoich partnerów o wymarzonym pomyśle wakacyjnym. '
                                                          'Dokończ powyższe zdanie i wygenerwuj plik do wstawienia '
                                                          'w stopkę maila.'}))
