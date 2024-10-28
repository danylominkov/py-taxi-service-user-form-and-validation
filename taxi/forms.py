from django import forms

from taxi.models import Driver


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["license_number"]

    def clean_license_number(self):
        license_number = self.cleaned_data.get("license_number")

        if Driver.objects.filter(license_number=license_number).exists():
            raise forms.ValidationError(
                "This license number is already taken."
            )

        if len(license_number) != 8:
            raise forms.ValidationError(
                "License number must be exactly 8 characters long."
            )

        if not license_number[:3].isalpha():
            raise forms.ValidationError(
                "The first three characters must be letters."
            )

        if not license_number[:3].isupper():
            raise forms.ValidationError(
                "The first three characters must be uppercase."
            )

        if not license_number[3:].isdigit():
            raise forms.ValidationError(
                "The last five characters must be digits."
            )

        return license_number
