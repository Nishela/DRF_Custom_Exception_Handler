__all__ = ("CustomHandlerSettings",)

from django.conf import settings

from .tools import import_from_string

import dataclasses


@dataclasses.dataclass
class CustomHandlerSettings:
    _user_settings: dict | None = dataclasses.field(default=None)
    _imported_user_settings: dict | None = dataclasses.field(default=None)

    @property
    def user_settings(self):
        if self._user_settings is None:
            self._user_settings = getattr(settings, 'CUSTOM_HANDLER', {})
        return self._user_settings

    @property
    def imported_user_settings(self):
        if self._imported_user_settings is None and self.user_settings:
            self._imported_user_settings = self.perform_imports()
        return self._imported_user_settings

    def perform_imports(self):
        imported_settings = {}
        for attr, value in self.user_settings.items():
            imported_attr = import_from_string(attr)
            imported_action = import_from_string(value)
            imported_settings[imported_attr] = imported_action
        return imported_settings
