siwes_platform/
│
├── manage.py
├── requirements.txt
├── .env
├── .env.example
├── README.md
│
├── config/ # Project settings & global configs
│ ├── **init**.py
│ ├── settings/
│ │ ├── **init**.py
│ │ ├── base.py
│ │ ├── dev.py
│ │ ├── prod.py
│ ├── urls.py
│ ├── wsgi.py
│ ├── asgi.py
│
├── shared/ # Reusable utilities & core modules
│ ├── **init**.py
│ ├── utils/
│ │ ├── exceptions.py
│ │ ├── response.py
│ │ ├── validators.py
│ │ ├── mixins.py
│ ├── middleware/
│ ├── permissions/
│ ├── enums.py
│ ├── constants.py
│
├── apps/
│ ├── **init**.py
│
│ ├── accounts/ # Users + auth + roles
│ │ ├── models.py
│ │ ├── serializers.py
│ │ ├── views.py
│ │ ├── urls.py
│ │ ├── services.py
│ │ ├── selectors.py
│ │ ├── permissions.py
│ │ ├── tasks.py
│ │ ├── signals.py
│
│ ├── institutions/ # University admin & policies
│ │ ├── models.py
│ │ ├── serializers.py
│ │ ├── views.py
│ │ ├── urls.py
│ │ ├── services.py
│ │ ├── selectors.py
│
│ ├── students/ # Profiles, placement lifecycle
│ │ ├── models.py
│ │ ├── serializers.py
│ │ ├── views.py
│ │ ├── urls.py
│ │ ├── services.py
│ │ ├── selectors.py
│
│ ├── supervisors/
│ │ ├── models.py
│ │ ├── serializers.py
│ │ ├── views.py
│ │ ├── urls.py
│ │ ├── services.py
│
│ ├── companies/ # Employer onboarding + verification
│ │ ├── models.py
│ │ ├── serializers.py
│ │ ├── views.py
│ │ ├── urls.py
│ │ ├── services.py
│ │ ├── verification.py
│
│ ├── marketplace/ # Placement listings & matching
│ │ ├── models.py
│ │ ├── serializers.py
│ │ ├── views.py
│ │ ├── urls.py
│ │ ├── services.py
│ │ ├── match_engine.py
│
│ ├── logbooks/ # Weekly reports + supervisor reviews
│ │ ├── models.py
│ │ ├── serializers.py
│ │ ├── views.py
│ │ ├── urls.py
│ │ ├── services.py
│
│ ├── workflows/ # Approvals, status pipelines
│ │ ├── models.py
│ │ ├── automations.py
│ │ ├── services.py
│ │ ├── events.py
│
│ ├── notifications/ # Email, SMS, in-app
│ │ ├── models.py
│ │ ├── templates/
│ │ ├── tasks.py
│ │ ├── services.py
│
│ ├── audits/ # Activity logs & compliance
│ │ ├── models.py
│ │ ├── services.py
│
└── tests/
├── **init**.py
├── factories/
├── integration/
├── unit/
