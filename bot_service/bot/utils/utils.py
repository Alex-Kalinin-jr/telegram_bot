from config import LANGUAGE, ADMIN_ID


def get_language() -> dict:
    from data.button_name import dict_names
    return dict_names[LANGUAGE]


def get_admin_messages() -> dict:
    from data.button_name import dict_messages
    return dict_messages[LANGUAGE]


def get_admins() -> list[int]:
    admins = [admin.strip() for admin in ADMIN_ID.split(",")]
    admins = [int(admin) for admin in admins if admin]

    return admins