import enum


@enum.unique
class Language(str, enum.Enum):
    BG = 'BG'
    EN = 'EN'

    def to_language(self) -> str:
        return {
            'BG': 'Bulgarian',
            'EN': 'English',
        }[self.value]

    def to_locale(self) -> str:
        return {
            'BG': 'bg_BG',
            'EN': 'en_US',
        }[self.value]

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]


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
