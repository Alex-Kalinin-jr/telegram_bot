from config import LANGUAGE


def get_language() -> str:
    from data.button_name import dict_names
    return dict_names[LANGUAGE]