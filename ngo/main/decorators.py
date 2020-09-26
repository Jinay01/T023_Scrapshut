from django.contrib.auth.decorators import user_passes_test

ngo_required = user_passes_test(lambda user: user.is_ngo, login_url='')
donor_required = user_passes_test(lambda user: user.is_donor, login_url='')
