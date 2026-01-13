from apps.supervisors.models import SupervisorProfile


def get_supervisors(request):
    supervisor_ids = request.data.get("supervisor_ids")
    institution = request.user.institutionprofile

    return SupervisorProfile.objects.filter(
        id__in=supervisor_ids, institution=institution
    )
