from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2024-02-01",  # Your API version
    azure_endpoint="https://mavericks-secureapi.azurewebsites.net/api/azureai",  # Your endpoint
    api_key="44adf48e1e147e62"  # Your API key
)

def extract_keywords_with_openai(text, description):
    prompt = (
        f"Analyze the following resume text and job description. "
        f"Extract the most relevant keywords from the resume based on the job description, "
        f"and also provide a percentage relevance score indicating how well the resume matches the job description. "
        f"nnResume Text: {text}nnJob Description: {description}nnKeywords and Relevance Score:"
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=100,
        top_p=0.6,
        frequency_penalty=0.7
    )
    result = response.choices[0].message.content.strip()
    return result


# Example usage
resume_text = """
Experienced software engineer with expertise in Python, Java, and cloud technologies.
Proven track record in developing scalable applications and leading development teams.
"""
job_description = """
We are looking for a software engineer with experience in Python, cloud technologies, and team leadership.
"""
keywords = extract_keywords_with_openai(resume_text, job_description)
print("Extracted Keywords:", keywords)
