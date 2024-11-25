from groq import Groq
def nlp_command(prompt):
    client = Groq(api_key='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')
    while True:
        
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "system",
                    "content": f"""You are an AI assistant for terminal commands. The user will input natural language requests to perform system operations, such as creating folders, files, or files with specific content (e.g., code). Your task is to respond with the exact terminal command to accomplish the request.  

                    Commands you can use:  
                    - **pwd**: Prints the current working directory.  
                    - **ls**: Lists files and directories in the current directory.  
                    - **cd [directory]**: Changes the current directory to the specified one.  
                    - **mkdir [directory_name]**: Creates a new directory.  
                    - **rmdir [directory_name]**: Removes an empty directory.  
                    - **touch [file_name]**: Creates a new empty file.  
                    - **rm [file_name]**: Deletes a file.  
                    - **rm -r [directory_name]**: Deletes a directory and its contents recursively.  
                    - **cp [source] [destination]**: Copies a file or directory to the specified destination.  
                    - **mv [source] [destination]**: Moves or renames a file or directory.  
                    - **echo '[content]' > [file_name]**: Creates a file with specified inner content.  
                    - **cat > [file_name] <<EOF ... EOF**: Creates a file and writes multiline content (e.g., code).  

                    Ensure commands are safe and non-malicious. Respond only with the command—no additional explanations.
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
        return out
