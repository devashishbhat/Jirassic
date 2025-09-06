
# Jirassic

## Overview
Jirassic is an AI-powered task management tool designed to revolutionize the way teams handle task assignments post-meetings. Our solution seamlessly converts meeting transcripts, audio, or video inputs into actionable tasks automatically assigned to the right teammates. By harnessing the power of AI, Jirassic eliminates the manual effort typically required for task distribution, enhancing productivity and efficiency.

## Features
- AI-powered task creation and assignment

- Automated speech-to-text transcription using Whisper

- Integration with Vertex AI’s Gemini-1.5 Pro for task identification

- FastAPI backend for efficient request handling

- MongoDB for secure data storage

- Next.js frontend with Tailwind CSS for a sleek UI

## How It Works
    A) Upload a meeting transcript, audio, or video file

    B) Whisper processes the input to generate an accurate transcript

    C) Vertex AI’s Gemini-1.5 Pro analyzes the transcript and extracts action items

    D) Tasks are assigned to the right team members based on context and skill matching

    E) Users can track tasks and manage project workflows efficiently


## Tech Stack
- Frontend: Next.js, Tailwind CSS

- Backend: Flask

- Database: MongoDB

- AI Models: Whisper (speech-to-text), Vertex AI Gemini-1.5 Pro (task assignment)

- Cloud Services: Google Cloud

## Getting Started
### Prerequisites
- Install Python 3.9 or 3.10

- Install Node.js and Yarn

- Set up a MongoDB database

- Obtain Google Cloud credentials for Vertex AI integration

### Installation
#### Backend Setup
```
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Frontend Setup
```
cd frontend
yarn install
yarn dev
```

### Running the Backend Servers
- Start the Flask Whisper server:
```
cd backend/whisper-server
python app.py
```

- Start the Flask core server:
```
cd backend/core-server
python app.py
```

## Contact
### For any inquiries or support, reach out via GitHub issues or contact us at:
- devashishbhat11@gmail.com
