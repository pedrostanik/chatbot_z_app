from openai import OpenAI
class AssistantGPT():
    def __init__(self):
        self.client = OpenAI()

    def execute(self, question):
        completion = self.client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
                {"role": "user", "content": question}
            ]
        )
        message = completion.choices[0].message
        answer = message.content
        print(f'answer: {answer}')
        return answer

if (__name__=='__main__'):
    assistant_gpt = AssistantGPT()
    assistant_gpt.execute()