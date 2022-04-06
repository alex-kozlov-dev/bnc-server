from bnc.settings import LANGUAGES

langs = [lang[0] for lang in LANGUAGES]


def i18nfields(fields: list[str]) -> list[str]:
    return [field + '_' + lang for field in fields for lang in langs]
