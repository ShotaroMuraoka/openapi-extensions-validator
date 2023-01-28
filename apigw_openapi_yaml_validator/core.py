import os, sys
import argparse
import yaml

from .rules.IntegrationRules import IntegrationRules

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('yaml', help='name of yaml file of open api to be verified')
    args = parser.parse_args()
    if args.yaml:
         print(f"the yaml of {args.yaml} ")

    ext = os.path.splitext(args.yaml)[1][1:]

    if ext not in ['yml', 'yaml']:
        print('extension error')
        # FIXME: Exceptionクラスを作成する
        exit(1)
    try:
        violations = []
        with open(args.yaml) as file:
            openapi = yaml.load(file, Loader=yaml.FullLoader)
            for path in openapi['paths']:
                if openapi['paths'][path] is None:
                    continue

                methods = openapi['paths'][path].keys()

                for method in methods:
                    if openapi['paths'][path][method] is None:
                        continue

                    rule = IntegrationRules()
                    violations.append(rule.validate(openapi['paths'][path][method], method))
        for violation in violations:
            # TODO: path, method, propertyを情報として返す
            if violation:
                print(violation)
            else:
                print('no violation')
    except Exception as e:
        print('Exception occurred while loading YAML...', file=sys.stderr)
        print(e, file=sys.stderr)
        exit(1)