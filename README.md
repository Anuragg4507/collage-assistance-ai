# College AI Assistant

A command-line college assistant powered by the Gemini API. The project also
includes tools for calculations, attendance records, timetable data, and
reading TXT, PDF, and DOCX files.

## Setup

1. Install Python 3.10 or newer.
2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your Gemini API key:

   ```text
   GEMINI_API_KEY=your_api_key_here
   ```

   Keep the real `.env` file private; it is excluded from Git.

## Run

```powershell
python app.py
```