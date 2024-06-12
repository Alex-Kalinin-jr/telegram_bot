from config import LANGUAGE


def get_language() -> dict:
    from data.button_name import dict_names
    return dict_names[LANGUAGE]


def get_admin_messages() -> dict:
    from data.button_name import dict_messages
    return dict_messages[LANGUAGE]