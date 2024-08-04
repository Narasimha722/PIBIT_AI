Extract and structure the resume information as JSON.


### Python Script

Here's a simple Python script using the OpenAI API to process the resume and parse the content into JSON format.

```python
import openai

# Replace with your own OpenAI API key
openai.api_key = "YOUR_API_KEY"

def parse_resume_to_json(resume_text):
    prompt = f"""
    You are an AI model that extracts structured information from resumes. Given a resume, parse its content into the following JSON format:

    ```json
    {{
      "name": "",
      "contact": {{
        "email": "",
        "phone": "",
        "linkedin": "",
        "github": ""
      }},
      "education": [
        {{
          "degree": "",
          "field_of_study": "",
          "university": "",
          "location": "",
          "start_date": "",
          "end_date": "",
          "cgpa": ""
        }}
      ],
      "experience": [
        {{
          "position": "",
          "company": "",
          "location": "",
          "start_date": "",
          "end_date": "",
          "responsibilities": [""]
        }}
      ],
      "projects": [
        {{
          "title": "",
          "description": "",
          "technologies": [""],
          "link": ""
        }}
      ],
      "certifications": [
        {{
          "name": "",
          "issuer": "",
          "date": "",
          "credential_id": ""
        }}
      ],
      "skills": [""]
    }}
    ```

    Here is a sample resume:

    ---
    {resume_text}
    ---

    Extract and structure the resume information as JSON.
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500
    )

    return response.choices[0].text.strip()

# Sample resume content
resume_text = """
Narasimha Reddy Asam 
Kadiri, Andhra Pradesh 515581 

www.linkedin.com/in/narasimha-reddy-asam-22m
narasimhareddyasam722@gmail.com 
https://github.com/Narasimha722
+91-7989937228 

Education 
Lovely Professional University Punjab 2021 – 2025 
Computer Science and Engineering — CGPA: 6.34 Jalandhar, Punjab 

Sri Chaitanya Jr College 2019 – 2021 
12th with Science — Percentage: 89.2% Tirupati, Andhra Pradesh 

Zilla Parishad High School 2018 – 2019 
10th with Science — Percentage: 93.5% Kadiri, Andhra Pradesh 

Experience 
Cipher Schools – E-Learning Platform May’23-Aug’23 
Gained expertise in fundamental data structures including stacks, queues, heaps, hash tables, and trees.

Projects 
End-to-End NLP Project with GitHub Action, MLOps, and Deployment [Text Summarization] May|24 
Developed an end-to-end text summarization application utilizing natural language processing techniques.

Skills 
Languages: C++, Python.
Technologies/Frameworks: Jenkins, Docker, Kubernetes, AWS, Git, GitHub, Linux, PyTorch, Scikit learn, Matplotlib, TensorFlow, Keras, Seaborn, spaCy, SciPy, NLTK, AWS SageMaker, LangChain.
Skills: Data Structures and Algorithms, Machine Learning, Natural Language Processing, Computer Vision, Deep Learning, MlOps.
"""

# Parse the resume to JSON
parsed_json = parse_resume_to_json(resume_text)
print(parsed_json)
