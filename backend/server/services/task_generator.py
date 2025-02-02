import os
from langchain_google_vertexai import VertexAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Step 1: Initialize Vertex AI
PROJECT_ID = "davidson-test-449321"
LOCATION = "us-central1"  # Use a supported region

# Global Variables
team_expertise = {
    "Alice": "Backend Development, API design",
    "Bob": "Frontend Development, UI/UX",
    "Charlie": "Database Management, SQL",
    "David": "DevOps, Cloud infrastructure"
}

template = """
You are a helpful assistant that analyzes a transcript of a team standup meeting and assigns tasks based on expertise and maximum allowed story points.

Here is the transcript:
{transcript}

Also, consider the team member's expertise when assigning tasks:
{team_expertise}

The total assigned story points for each team member should be less the maximum allowed story points which is 24.
In a case where the total assigned stry points are going to go above the threshold which is 24, then assign the user story to a different team member with similar expertise.

Please assign each task to the appropriate team member, and provide the result as a JSON object with two attributes: "team_member_name" and "task_assigned" and "story points" estimation that task.
"""

prompt = PromptTemplate(
    input_variables=["transcript", "team_expertise"],
    template=template
)

def assign_tasks_from_transcript(transcript : str):
    # Step 5: Create the VertexAI LLM instance
    vertex_ai_llm = VertexAI(
        model_name="gemini-1.0-pro",
        project=PROJECT_ID,
        location=LOCATION,
        max_output_tokens=256,
        temperature=0.2,
        top_p=0.8,
        top_k=40
    )

    # Step 6: Create the LangChain chain
    llm_chain = LLMChain(prompt=prompt, llm=vertex_ai_llm)

    # Step 7: Run the chain with the global transcript and team expertise
    output = llm_chain.run({
        "transcript": transcript,
        "team_expertise": team_expertise
    })

    # Step 8: Return the result (this will be in JSON format)
    return output
