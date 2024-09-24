from django import forms

class EncryptionForm(forms.Form):
    data = forms.CharField(label='Data to Encrypt', widget=forms.Textarea, required=True)
    key_size = forms.ChoiceField(choices=[('128', '128'), ('192', '192'), ('256', '256')], label='Key Size')
    mode = forms.ChoiceField(choices=[('ECB', 'ECB'), ('CBC', 'CBC'), ('CFB', 'CFB'), ('OFB', 'OFB')], label='Mode')
    custom_key = forms.CharField(label='Custom Key (Optional)', required=False)
    custom_iv = forms.CharField(label='Custom IV (Optional, for CBC, CFB, OFB)', required=False)

class DecryptionForm(forms.Form):
    encrypted_data = forms.CharField(label='Encrypted Data (hex)', widget=forms.Textarea, required=True)
    key_size = forms.ChoiceField(choices=[('128', '128'), ('192', '192'), ('256', '256')], label='Key Size')
    mode = forms.ChoiceField(choices=[('ECB', 'ECB'), ('CBC', 'CBC'), ('CFB', 'CFB'), ('OFB', 'OFB')], label='Mode')
    custom_key = forms.CharField(label='Custom Key', required=True)
    custom_iv = forms.CharField(label='Custom IV (for CBC, CFB, OFB)', required=False)
