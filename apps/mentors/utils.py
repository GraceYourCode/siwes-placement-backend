from apps.logbooks.models import LogbookEntry


def get_students_entries(request):
    mentor = request.user.companymentor
    entry_ids = request.data.get("entry_ids")
    return LogbookEntry.objects.filter(id__in=entry_ids, placement__mentor=mentor)
