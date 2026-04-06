import json

def rename_keys(data, key_map):
    if isinstance(data, list):
        return [rename_keys(item, key_map) for item in data]
    if isinstance(data, dict):
        new_dict = {}
        for k, v in data.items():
            new_key = key_map.get(k, k)
            new_dict[new_key] = rename_keys(v, key_map)
        return new_dict
    return data

def process_json(input_file, output_file, key_map):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    transformed = rename_keys(data, key_map)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(transformed, f, indent=4)

key_mapping = {
    "name": "full_name",
    "age": "user_age",
    "email": "contact_email"
}

process_json('input.json', 'output.json', key_mapping)
