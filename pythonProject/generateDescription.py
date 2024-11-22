from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2024-02-01",  # Your API version
    azure_endpoint="https://mavericks-secureapi.azurewebsites.net/api/azureai",  # Your endpoint
    api_key="44adf48e1e147e62"  # Your API key
)

def generate_job_description(title, department, location, employment_type, salary, qualification):
    prompt = f"Generate a job requirement description for a {title} in the {department} sector, for {location} location, for {employment_type} working, expected salary {salary}, minimum qualification needed for the job is {qualification}"
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"You are a helpful assistant"},
            {"role":"user","content":prompt}
        ],
        temperature=0.7,
        max_tokens=256,
        top_p=0.6,
        frequency_penalty=0.7
    )
    description = res.choices[0].message.content
    return description

job_title="Software Engineer"
job_department="IT"
job_location="Mumbai"
job_employment_type="Full time"
job_salary="6 lpa"
job_qualification="B Tech + M Tech"

job_description = generate_job_description(job_title, job_department, job_location, job_employment_type, job_salary, job_qualification)
print(job_description)

