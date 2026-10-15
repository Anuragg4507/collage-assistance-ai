import os
import time

from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing from .env file"
    )


# Gemini API Client
client = genai.Client(
    api_key=GEMINI_API_KEY
)


# Model
MODEL = "gemini-3.8-flash"


def ask_llm(prompt: str):
    for attempt in range(4):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
                config={
                    "system_instruction": (
                        "You are a helpful College AI Assistant. "
                        "Answer students clearly and simply."
                    ),
                    "max_output_tokens": 500
                }
            )
            return response.text
        except Exception as exc:
            status_code = getattr(exc, "status_code", None)
            if status_code is None:
                status_code = getattr(exc, "code", None)
            is_unavailable = (
                status_code == 503
                or getattr(exc, "status", None) == "UNAVAILABLE"
            )

            if not is_unavailable:
                raise
            if attempt == 3:
                raise RuntimeError(
                    "Gemini is still experiencing high demand after "
                    "3 retries. Please wait a little and try again."
                ) from exc

            time.sleep(2 ** attempt)


if __name__ == "__main__":

    question = input("Ask College AI: ")

    try:

        answer = ask_llm(question)

        print("\nAI Response:")
        print(answer)

    except Exception as e:

        print("\nERROR:")
        print(e)