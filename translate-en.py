import os
import subprocess
from openai import OpenAI
import time

# Run the setenv.sh script
os.system('source ignore/setenv.sh')

# Read the API key, assistant ID, and organization ID from environment variables
api_key = os.getenv('OPENAI_API_KEY')
assistant_id = os.getenv('OPENAI_ASSISTANT_EN')
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

def pretty_print(messages):
    print("# Messages")
    for m in messages:
        print(f"{m.role}: {m.content[0].text.value}")
    print()

def get_translated_text(messages):
    # Initialize an empty string to store the translated text
    translated_text = ""
    # Loop through each message object
    for m in messages:
        # Check if the message is from the assistant (i.e., the translated text)
        if m.role == "assistant":
            # Concatenate the message content to the translated_text string
            for component in m.content:
                if component.text and component.text.value:
                    translated_text += component.text.value
    return translated_text

# Waiting in a loop
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
    if f.endswith('-es.md') and 'chapter' in f and os.path.exists(f): # Only Spanish chapters (ignore the tracked as deleted)
        filename = os.path.join(os.path.dirname(f).replace('/es/', '/en/'), os.path.basename(f).replace('-es.md', '-en.md')) # destination filename
        print(f"Translating {f} to {filename}")
        with open(f, 'r') as file:
            text = file.read()
            print(f"Original text: {text}")
            thread, run = create_thread_and_run(text)
            run = wait_on_run(run, thread)
            translated_text = get_translated_text(get_response(thread))
            with open(filename, 'w') as out_file:
                out_file.write(translated_text + '\n\n')  # Add two empty lines at the end
                print(f"Translation completed for {f}")
