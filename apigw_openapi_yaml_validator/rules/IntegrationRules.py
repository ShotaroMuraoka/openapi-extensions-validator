from .IValidationRules import IValidationRules
import json

class IntegrationRules(IValidationRules):
    EXTENSION_OBJECT_NAME = 'x-amazon-apigateway-integration'

    def integration_properties(self):
        return [
            'cacheKeyParameters',
            'cacheNamespace',
            'connectionId',
            'connectionType',
            'credentials',
            'contentHandling',
            'httpMethod',
            'integrationSubtype',
            'passthroughBehavior',
            'payloadFormatVersion',
            'requestParameters',
            'requestTemplates',
            'responses',
            'timeoutInMillis',
            'type',
            'tlsConfig',
            'uri',
        ]

    def validate(self, operation_object, method):
        if (operation_object[self.EXTENSION_OBJECT_NAME] is None):
            return []

        integration = operation_object[self.EXTENSION_OBJECT_NAME]

        for property in self.integration_properties():
            integration.pop(property, None)
        # print(json.dumps(integration, indent=2))

        if integration:
            print('==Invalid property found out')
            # print(integration)
            invalid_properties = []
            for invalid_property in integration.keys():
                invalid_properties.append(invalid_property)
                # print(invalid_property)
            return [self.EXTENSION_OBJECT_NAME, method, invalid_properties]
        return []

