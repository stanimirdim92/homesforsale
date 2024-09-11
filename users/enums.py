import enum


@enum.unique
class Language(str, enum.Enum):
    bg = 'bg'
    en = 'en'

    def to_language(self) -> str:
        return {
            'bg': 'Bulgarian',
            'en': 'English',
        }[self.value]

    def to_locale(self) -> str:
        return {
            'bg': 'bg_BG',
            'en': 'en_US',
        }[self.value]


@enum.unique
class Types(str, enum.Enum):
    CLIENT = 'CLIENT'
    AGENCY = 'AGENCY'
    AGENT = 'AGENT'
    ORGANIZATION = 'ORGANIZATION'

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]

@enum.unique
class Titles(str, enum.Enum):
    MR = 'Mr'
    MRS = 'Mrs'
    MISS = 'Miss'
    MS = 'Ms'
    DR = 'Dr'
    PROF = 'Prof'
    SIR = 'Sir'

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]
