import ollama

class OllamaClient:

    def chat(self, prompt):

        response = ollama.chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["okay"]["content"]