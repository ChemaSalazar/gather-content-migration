from dotenv import load_dotenv
import os

load_dotenv()

# Other mime types for the API is default_mime = 'application/vnd.gathercontent.v0.5+json'
default_mime = 'application/vnd.gathercontent.v2+json'

gc_url = 'https://api.gathercontent.com/'

# Add your custom field types to this list.
field_type = ["text", "choice_checkbox"]

workflow_status = os.environ["workflow_status"] # Dictionary with workflow labels and assoc IDs from Gather Content

nextproject = os.environ["nextproject"]  # ID integer for next Gather Content project
maxcycles = 1
