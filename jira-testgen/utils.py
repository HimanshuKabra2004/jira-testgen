import os
import openai
from dotenv import load_dotenv
from datetime import datetime
import logging

# ---------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# ---------------------------------------------------
# ---------------------------------------------------
# Setup Logging
# ---------------------------------------------------
os.makedirs("logs", exist_ok=True)  # Ensure logs directory exists

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)
import os
import openai
from dotenv import load_dotenv
from datetime import datetime
import logging

# ---------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# ---------------------------------------------------
# Setup Logging
# ---------------------------------------------------
os.makedirs("logs", exist_ok=True)  # Ensure logs directory exists

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

# ---------------------------------------------------
# Generate Test Cases from Jira Ticket Description
# ---------------------------------------------------
def generate_test_cases(description, model="gpt-3.5-turbo"):
    """
    Use OpenAI's Chat API to generate test cases based on a Jira ticket description.

    Parameters:
        description (str): Jira ticket description.
        model (str): GPT model to use (default: gpt-3.5-turbo).

    Returns:
        str: Generated test cases in Gherkin format or error message.
    """
    try:
        logging.info("Generating test cases using OpenAI API...")

        prompt = f"""
Generate test scenarios and test cases for this Jira ticket:
\"\"\"
{description}
\"\"\"

Organize the result into:
- Positive cases
- Negative cases
- Edge/Boundary cases

Format each test case using:
**Given / When / Then** format.
"""

        messages = [
            {"role": "system", "content": "You are a professional QA engineer that writes clear and comprehensive test cases in Gherkin format."},
            {"role": "user", "content": prompt}
        ]

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=1500,
            temperature=0.3,
        )

        content = response.choices[0].message.content.strip()
        logging.info("Test case generation completed successfully.")
        return content

    except openai.error.OpenAIError as e:
        error_msg = f"❌ OpenAI Error: {str(e)}"
        logging.error(error_msg)
        return error_msg
    except Exception as e:
        error_msg = f"❌ Error generating test cases: {str(e)}"
        logging.error(error_msg)
        return error_msg

# ---------------------------------------------------
# Save Generated Test Cases to Markdown
# ---------------------------------------------------
def save_to_markdown(content, filename=None):
    """
    Save generated test cases to a markdown file.

    Parameters:
        content (str): Test case content.
        filename (str): Optional filename. If not provided, timestamped filename will be used.
    
    Returns:
        str: Full path to the saved markdown file.
    """
    try:
        os.makedirs("output", exist_ok=True)
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            filename = f"test_cases_{timestamp}.md"

        file_path = os.path.join("output", filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("# 🧪 AI-Generated Test Cases\n\n")
            f.write(content)

        logging.info(f"Test cases saved to {file_path}")
        return file_path

    except Exception as e:
        logging.error(f"❌ Error saving file: {str(e)}")
        return f"❌ Failed to save file: {str(e)}"

# Example usage
if __name__ == "__main__":
    description = "This is a sample Jira ticket description."
    test_cases = generate_test_cases(description)
    save_to_markdown(test_cases)
# ---------------------------------------------------
# Generate Test Cases from Jira Ticket Description
# ---------------------------------------------------
def generate_test_cases(description, model="gpt-3.5-turbo"):
    """
    Use OpenAI's Chat API to generate test cases based on a Jira ticket description.

    Parameters:
        description (str): Jira ticket description.
        model (str): GPT model to use (default: gpt-3.5-turbo).

    Returns:
        str: Generated test cases in Gherkin format or error message.
    """
    try:
        logging.info("Generating test cases using OpenAI API...")

        prompt = f"""
Generate test scenarios and test cases for this Jira ticket:
\"\"\"
{description}
\"\"\"

Organize the result into:
- Positive cases
- Negative cases
- Edge/Boundary cases

Format each test case using:
**Given / When / Then** format.
"""

        messages = [
            {"role": "system", "content": "You are a professional QA engineer that writes clear and comprehensive test cases in Gherkin format."},
            {"role": "user", "content": prompt}
        ]

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=1500,
            temperature=0.3,
        )

        content = response.choices[0].message.content.strip()
        logging.info("Test case generation completed successfully.")
        return content

    except Exception as e:
        error_msg = f"❌ Error generating test cases: {str(e)}"
        logging.error(error_msg)
        return error_msg

# ---------------------------------------------------
# Save Generated Test Cases to Markdown
# ---------------------------------------------------
def save_to_markdown(content, filename=None):
    """
    Save generated test cases to a markdown file.

    Parameters:
        content (str): Test case content.
        filename (str): Optional filename. If not provided, timestamped filename will be used.
    
    Returns:
        str: Full path to the saved markdown file.
    """
    try:
        os.makedirs("output", exist_ok=True)
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            filename = f"test_cases_{timestamp}.md"

        file_path = os.path.join("output", filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("# 🧪 AI-Generated Test Cases\n\n")
            f.write(content)

        logging.info(f"Test cases saved to {file_path}")
        return file_path

    except Exception as e:
        logging.error(f"❌ Error saving file: {str(e)}")
        return f"❌ Failed to save file: {str(e)}"
