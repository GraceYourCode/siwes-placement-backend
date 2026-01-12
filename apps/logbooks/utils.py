from django.core.exceptions import PermissionDenied


def if_not_student_restrict_other_users(user, action):
    if user.role != "student":
        raise PermissionDenied(f"Only students can {action} logbook entries")
