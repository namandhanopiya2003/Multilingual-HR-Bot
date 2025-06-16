import json
import os

def load_txt_knowledge(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def load_json_knowledge(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_all_hr_knowledge(knowledge_folder: str = 'hr_knowledge'):
    knowledge = {}
    for filename in os.listdir(knowledge_folder):
        path = os.path.join(knowledge_folder, filename)
        if filename.endswith('.txt'):
            knowledge[filename] = load_txt_knowledge(path)
        elif filename.endswith('.json'):
            knowledge[filename] = load_json_knowledge(path)
    return knowledge
