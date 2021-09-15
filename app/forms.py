from django import forms


class ResumeForm(forms.Form):

    full_name = forms.CharField(
        label='Enter Full Name', max_length=100, required=False)
    address = forms.CharField(label='Address', max_length=250, required=False)
    phone = forms.RegexField(label='Phone no',
                             regex=r'^\+?1?\d{9,15}$', error_messages={'Error': "Enter Valid phone number"}, required=False)
    email = forms.EmailField(label='Email Id', max_length=150, required=False)
    about_you = forms.CharField(
        label='About You', max_length=400, required=False)
    education = forms.CharField(
        label='Education Details', max_length=250, required=False)
    career = forms.CharField(label='Career', max_length=150, required=False)
    job_1_start = forms.DateField(
        widget=forms.SelectDateWidget, required=False)
    job_1_end = forms.DateField(
        widget=forms.SelectDateWidget, required=False)
    job_1_details = forms.CharField(max_length=250, required=False)
    job_2_start = forms.DateField(
        widget=forms.SelectDateWidget, required=False)
    job_2_end = forms.DateField(
        widget=forms.SelectDateWidget, required=False)
    job_2_details = forms.CharField(max_length=250, required=False)
    job_3_start = forms.DateField(
        widget=forms.SelectDateWidget, required=False)
    job_3_end = forms.DateField(
        widget=forms.SelectDateWidget, required=False)
    job_3_details = forms.CharField(max_length=250, required=False)
    references = forms.CharField(
        label='References', max_length=250, required=False)
    image = forms.ImageField(required=False)
