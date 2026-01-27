import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_car_description(brand, model, year):
    model_id = "llama-3.3-70b-versatile"

    prompt = (
        f"Act as a professional car copywriter. Write a 2-sentence catchy "
        f"description for a {year} {brand} {model} for a car dealership website."
    )

    try:
        completion = client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=100,
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error calling Groq: {e}")
        return "A beautiful car that fits your lifestyle."
