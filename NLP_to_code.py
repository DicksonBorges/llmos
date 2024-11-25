from groq import Groq
import re
def nlp_code(prompt):
    client = Groq(api_key='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')
    while True:
        
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "system",
                    "content": f""" You are an AI assistant specializing in generating Python code. 
                    Based solely on user queries, you will produce precise and functional Python scripts or snippets that address the user's request. 
                    No explanations, no commentary—just clean, efficient Python code tailored to the task at hand. 
                    Your goal is to deliver top-quality solutions in Python, staying strictly focused on the requested functionality.
                    """
                },
                {
                "role": "user",
                "content": prompt
            }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        out = ""
        for chunk in completion:
            print(chunk.choices[0].delta.content or "", end="")
            out+=chunk.choices[0].delta.content or ''
            matches = re.findall(r"```(.*?)```", out, re.DOTALL)
        return str(matches[0])
exec(nlp_code("write a code to count the number of files in the '/Users/dicksonborges/Desktop/major_project/vaibhav' directory"))