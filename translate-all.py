import os
import subprocess
from openai import OpenAI
import time

# Run the setenv.sh script
os.system('source ignore/setenv.sh')

# Read the API key, assistant ID, and organization ID from environment variables
api_key = os.getenv('OPENAI_API_KEY')
assistant_id = os.getenv('OPENAI_ASSISTANT_ALL')
organization_id = os.getenv('OPENAI_ORGANIZATION_ID')

# Create an OpenAI object with the API key and the organization ID
client = OpenAI(api_key=api_key, organization=organization_id)

# Assistant functions
def submit_message(assistant_id, thread, user_message):
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=user_message
    )
    return client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )

def get_response(thread):
    return client.beta.threads.messages.list(thread_id=thread.id, order="asc")

def create_thread_and_run(user_input):
    thread = client.beta.threads.create()
    run = submit_message(assistant_id, thread, user_input)
    return thread, run

def get_translated_text(messages):
    english_translation = ""
    german_translation = ""
    is_english = False
    is_german = False
    for m in messages:
        if m.role == "assistant":
            for component in m.content:
                if component.text and component.text.value:
                    line = component.text.value
                    if line.strip() == "=== BEGIN ENGLISH TRANSLATION ===":
                        is_english = True
                    elif line.strip() == "=== BEGIN GERMAN TRANSLATION ===":
                        is_german = True
                    elif line.strip() == "=== END ENGLISH TRANSLATION ===":
                        is_english = False
                    elif line.strip() == "=== END GERMAN TRANSLATION ===":
                        is_german = False
                    elif is_english:
                        english_translation += line
                    elif is_german:
                        german_translation += line
    return english_translation, german_translation

def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

# Step 0. Translate all markdown files ending in -es.md that have changed
changed_files = subprocess.check_output(['git', 'diff', '--name-only', '--cached']).decode().splitlines()
for f in changed_files:
    if f.endswith('-es.md') and os.path.exists(f):
        with open(f, 'r') as file:
            text = file.read()
            thread, run = create_thread_and_run(text)
            run = wait_on_run(run, thread)
            english_translation, german_translation = get_translated_text(get_response(thread))
            english_filename = f.replace('-es.md', '-en.md')
            german_filename = f.replace('-es.md', '-de.md')
            with open(english_filename, 'w') as out_file:
                out_file.write(english_translation)
                print(f"English translation completed for {f}")
            with open(german_filename, 'w') as out_file:
                out_file.write(german_translation)
                print(f"German translation completed for {f}")
