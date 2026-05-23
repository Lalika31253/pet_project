def get_user_role(user):
    if user.is_superuser:
        return "admin"

    if user.groups.filter(name="Shelter Staff").exists():
        return "staff"

    return "user"