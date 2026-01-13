from apps.companies.models import Company


def placement_letter_upload_path(instance, filename):
    return f"institution_{instance.institution.id}/placements/student_{instance.student.matric_no}/company_{instance.company.id}/{filename}"


def get_company(company_id):
    return Company.objects.get(pk=company_id)
