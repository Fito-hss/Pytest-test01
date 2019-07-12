import yaml


def read():
    with open('./data/data.yaml', 'r', encoding='utf-8') as f:
        return yaml.load(f)
