import yaml

with open("environment.yml") as fp:
    d = yaml.safe_load(fp)

print(d)