from apps.students.models import StudentPlacement


def get_placements(request):
    placement_ids = request.data.get("placement_ids")
    supervisor = request.user.institutionprofile

    return StudentPlacement.objects.filter(id__in=placement_ids, supervisor=supervisor)
