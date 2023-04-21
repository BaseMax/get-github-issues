# Get GitHub Issues

A Python script to get a list of all open issues in a repository with specific labels, and fetch their corresponding bodies and comments in chronological order (oldest to newest).

## Prerequisites

- Python 3.x
- GitHub Personal Access Token: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

## Installation

Clone the repository:
```bash
git clone https://github.com/BaseMax/get-github-issues.git
cd get-github-issues
```

Create an virtual envirement:
```console
python -m venv venv
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

At last run activate binary file to enable virtual envirenment:
```console
source venv/bin/activate
```

## Usage

Set the ACCESS_TOKEN (GitHub Personal Access Token) variable inside `.env` file:

Or
```bash
export ACCESS_TOKEN=YOUR_TOKEN_HERE
```

Run the script:
```bash
python script.py <owner> <repository> <labels>
```

Replace <owner> with the name of the repository owner, <repository> with the name of the repository, and <labels> with a comma-separated list of labels you want to filter by. For example:

```bash
python get-github-issues.py BaseMax get-github-issues "bug,enhancement"
```
  
This will fetch all open issues in the BaseMax/get-github-issues repository with the labels "bug" or "enhancement".

## License

This project is licensed under the GPL-3.0 License - see the LICENSE file for details.

## Acknowledgments

- GitHub REST API v3
- python-dotenv

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

Copyright 2023, Max Base
