import os, sys
import argparse
import yaml

from .rules.x_amazon_apigateway_integration_rules import IntegrationRules
from .rules.x_amazon_apigateway_integrations_rules import IntegrationsRules


def rule_instances() -> list:
    return [
        IntegrationRules(),
        IntegrationsRules(),
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("yaml", help="name of yaml file of open api to be verified")
    args = parser.parse_args()
    ext = os.path.splitext(args.yaml)[1][1:]

    if ext not in ["yml", "yaml"]:
        print(f"Warning: {args.yaml} is not YAML file")
        exit(1)

    try:
        violations = []
        with open(args.yaml) as file:
            openapi_yaml = yaml.load(file, Loader=yaml.FullLoader)
            for rule in rule_instances():
                violation = rule.validate(openapi_yaml)
                if violation:
                    violations.append(violation)
        if len(violations) == 0:
            print("No invalid properties found")
            exit(0)
        for violation in violations:
            for invalids in violation:
                if invalids:
                    for invalid_property in invalids["invalid_properties"]:
                        print(
                            "invalid property:",
                            invalids["path"],
                            invalids["method"],
                            invalids["object_name"],
                            invalid_property,
                        )
    except Exception as e:
        print("Exception occurred while loading YAML...", file=sys.stderr)
        print(e, file=sys.stderr)
        exit(1)
