import enum

from django.utils.translation import gettext_lazy as _


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
        return [(item.value, item.to_language()) for item in cls]


@enum.unique
class Currency(str, enum.Enum):
    EUR = 'EUR'
    GBP = 'GBP'
    BGN = 'BGN'
    CHF = 'CHF'

    def to_symbol(self) -> str:
        return {
            'EUR': '€',
            'GBP': '£',
            'BGN': 'лв.',
            'CHF': 'CHF',

        }[self.value]

    def to_name(self) -> str:
        return {
            'EUR': _('Euro'),
            'GBP': _('Pound Sterling'),
            'BGN': _('Bulgarian Lev'),
            'CHF': _('Swiss Franc'),
        }[self.value]

    @classmethod
    def choices(cls):
        return [(item.value, str(item.to_name() + ' (' + item.to_symbol() + ')')) for item in cls]


@enum.unique
class UserTypes(str, enum.Enum):
    CLIENT = 'CLIENT'
    REALTOR = 'REALTOR'
    AGENT = 'AGENT'

    def to_name(self) -> str:
        return {
            'CLIENT': _('Client'),
            'REALTOR': _('Realtor/Agency'),
            'AGENT': _('Real Estate Agent'),
        }[self.value]

    @classmethod
    def choices(cls):
        return [(item.value, item.to_name()) for item in cls]


@enum.unique
class Titles(str, enum.Enum):
    MR = 'Mr'
    MRS = 'Mrs'
    MISS = 'Miss'
    MS = 'Ms'
    DR = 'Dr'
    PROF = 'Prof'
    SIR = 'Sir'

    def to_name(self) -> str:
        return {
            'MR': _('Mr'),
            'MRS': _('Mrs'),
            'MISS': _('Miss'),
            'MS': _('Ms'),
            'DR': _('Dr'),
            'PROF': _('Prof'),
            'SIR': _('Sir'),
        }[self.name]

    @classmethod
    def choices(cls):
        return [(item.value, item.to_name()) for item in cls]
