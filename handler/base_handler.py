__all__ = ("CustomExceptionHandler",)

import dataclasses
from .base_settings import CustomHandlerSettings
from rest_framework.views import exception_handler

from .tools import import_from_string


@dataclasses.dataclass
class CustomExceptionHandler:
    custom_settings: type[CustomHandlerSettings] | str = dataclasses.field(
        default_factory=lambda: CustomHandlerSettings())

    def __post_init__(self):
        if isinstance(self.custom_settings, str):
            self._settings_instance = import_from_string(self.custom_settings)()
        else:
            self._settings_instance = self.custom_settings
        self._imported_user_settings = self._settings_instance.imported_user_settings

    def __call__(self, exc, context):
        response = exception_handler(exc, context)
        if response is None and self._imported_user_settings:
            response = self.handle_custom_exception(exc, context)
        return response

    def handle_custom_exception(self, exc, context):
        handler = self._imported_user_settings.get(type(exc))

        if handler:
            return handler(exc, context)

        for exc_type, handler in self._imported_user_settings.items():
            if isinstance(exc, exc_type):
                return handler(exc, context)

        return None
