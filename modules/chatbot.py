from modules.translation import detect_language, translate_to_english, translate_from_english
from modules.openai_api import ask_gpt
from modules.hr_knowledge_loader import load_all_hr_knowledge

class HRChatbot:
    def __init__(self):
        self.hr_knowledge = load_all_hr_knowledge()
        self.short_term_memory = []  # Stores recent messages for context

    def build_context(self):
        # Create system context embedding HR knowledge (can be expanded to vector search)
        context_str = "Here is some company HR info:\n"
        for k, v in self.hr_knowledge.items():
            if isinstance(v, dict):
                context_str += f"{k}:\n"
                for key, val in v.items():
                    context_str += f"- {key}: {val}\n"
            else:
                context_str += f"{v}\n"
        return [{"role": "system", "content": context_str}]

    def chat(self, user_input: str) -> str:
        # Detect language
        user_lang = detect_language(user_input)

        # Translate user input to English for GPT
        english_input = translate_to_english(user_input, user_lang)

        # Build chat context with HR knowledge + recent chat memory
        context = self.build_context()
        context.extend(self.short_term_memory)

        # Get GPT response in English
        gpt_response_english = ask_gpt(english_input, context)

        # Translate response back to user language
        translated_response = translate_from_english(gpt_response_english, user_lang)

        # Update short-term memory for context (last 6 messages approx)
        self.short_term_memory.append({"role": "user", "content": english_input})
        self.short_term_memory.append({"role": "assistant", "content": gpt_response_english})
        if len(self.short_term_memory) > 12:
            self.short_term_memory = self.short_term_memory[-12:]

        return translated_response
