import abc

class IValidationRules(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def validate(self, openapi_yaml) -> list:
        pass