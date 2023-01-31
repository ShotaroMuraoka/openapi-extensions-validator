from .IValidationRules import IValidationRules

class IntegrationRules(IValidationRules):
    EXTENSION_OBJECT_NAME = 'x-amazon-apigateway-integration'

    def extension_properties(self) -> list:
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

    def validate(self, openapi_yaml) -> list:
        invalids = []
        for path in openapi_yaml['paths']:
            if openapi_yaml['paths'][path] is None:
                continue

            methods = openapi_yaml['paths'][path].keys()

            for method in methods:
                if openapi_yaml['paths'][path][method] is None:
                    continue

                operation_object = openapi_yaml['paths'][path][method]

                if (operation_object[self.EXTENSION_OBJECT_NAME] is None):
                    continue

                extension_object = operation_object[self.EXTENSION_OBJECT_NAME]

                for property in self.extension_properties():
                    extension_object.pop(property, None)

                if extension_object:
                    invalid_properties = []
                    for invalid_property in extension_object.keys():
                        invalid_properties.append(invalid_property)

                    invalids.append({
                        'path': path,
                        'method': method,
                        'object_name': self.EXTENSION_OBJECT_NAME,
                        'invalid_properties': invalid_properties
                    })
        return invalids
