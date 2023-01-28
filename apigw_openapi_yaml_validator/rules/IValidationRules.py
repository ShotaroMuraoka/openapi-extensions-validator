import abc

class IValidationRules(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def validate(self, operation_object, method):
        return []