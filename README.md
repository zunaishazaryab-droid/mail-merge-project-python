# mail-merge-project-python

## Project Description
This project is a Python-based mail merge tool that automates the process of creating personalized emails or letters by merging a template with a list of recipient data.

## Features
- Load recipient data from a file.
- Use a customizable template for messages.
- Generate personalized messages for each recipient.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mail-merge-project
   ```
2. Ensure you have Python installed (version 3.6 or higher).
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Prepare a template file (e.g., `template.txt`) with placeholders for personalization.
2. Provide a recipient data file (e.g., `recipients.csv`) containing the necessary information.
3. Run the script:
   ```bash
   python mail_merge.py
   ```
4. The personalized messages will be generated in the output directory.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
