# PricePlanDRF

First install required DRF libraries using:
  pip install djangorestframework
  pip install markdown       # Markdown support for the browsable API.
  pip install django-filter  # Filtering support

Add 'rest_framework' to your INSTALLED_APPS setting.
  INSTALLED_APPS = [
  
    'rest_framework',
  ]

"apps": "http://127.0.0.1:8000/apps/",
'apps' path will add the user with their name and description

"plans": "http://127.0.0.1:8000/plans/",
'plans' path will add plan name and their respective price  ('Free', 'Free ($0)'), ('Standard', 'Standard ($10)'), ('Pro', 'Pro ($25)'),

"subscriptions": "http://127.0.0.1:8000/subscriptions/"
'subscriptions' path will fetch username and their price plan (with 'Active' mark)
