from ..models.x_amazon_apigateway_integration import XAmazonApigatewayIntegration
import re


class IntegrationRules:
    EXTENSION_OBJECT_NAME = "x-amazon-apigateway-integration"

    def validate(self, openapi_yaml) -> list:
        invalids = []
        for path in openapi_yaml["paths"]:
            if openapi_yaml["paths"][path] is None:
                continue

            methods = openapi_yaml["paths"][path].keys()
            for method in methods:
                if openapi_yaml["paths"][path][method] is None:
                    continue

                operation_object = openapi_yaml["paths"][path][method]

                if operation_object[self.EXTENSION_OBJECT_NAME] is None:
                    continue

                try:
                    XAmazonApigatewayIntegration(
                        **operation_object[self.EXTENSION_OBJECT_NAME]
                    )
                except TypeError as te:
                    # print('######type error')
                    invalids.append(
                        {
                            "path": path,
                            "method": method,
                            "object_name": self.EXTENSION_OBJECT_NAME,
                            "invalid_properties": re.findall(r"\'(.*)\'", te.args[0])
                            # TODO: return which violation. (invalid propery name or invalid value)
                        }
                    )
                    # TODO: invalid propertyとpath, methodをここで注入する
                except ValueError as ve:
                    # print('####value error')
                    invalids.append(
                        {
                            "path": path,
                            "method": method,
                            "object_name": self.EXTENSION_OBJECT_NAME,
                            "invalid_properties": [ve.args[0]]
                            # TODO: return which violation. (invalid propery name or invalid value)
                        }
                    )
        return invalids
