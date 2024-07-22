Here’s the corrected and complete `README.md` file combining both tasks:

```markdown
# Task 1
## Cow Wisdom Web Server

### Prerequisites

Install the necessary packages:

```sh
sudo apt install fortune-mod cowsay -y
```

### How to Use

1. Run `./wisecow.sh`
2. Point your browser to the server port (default is 4499)

### What to Expect

![wisecow](https://github.com/nyrahul/wisecow/assets/9133227/8d6bfde3-4a5a-480e-8d55-3fef60300d98)

## Problem Statement

Deploy the wisecow application as a Kubernetes (k8s) app.

### Requirements

1. Create a Dockerfile for the image and the corresponding Kubernetes manifest to deploy in a k8s environment. The wisecow service should be exposed as a k8s service.
2. Set up a GitHub Action to create a new image when changes are made to this repository.
3. **Challenge Goal:** Enable secure TLS communication for the wisecow app.

### Expected Artifacts

1. GitHub repository containing the app with the corresponding Dockerfile, Kubernetes manifest, and any other necessary artifacts.
2. GitHub repository with the corresponding GitHub Action.
3. The GitHub repository should be kept private and access should be granted to the following GitHub IDs: nyrahul, SujithKasireddy.

---

# Task 2
## Log File Analyzer

This repository contains a Python script to analyze web server logs. The script performs the following tasks:

1. Counts the number of 404 errors in the log file.
2. Identifies the most requested pages.
3. Lists the most frequent IP addresses making requests.

### Prerequisites

- Python 3.12 or higher
- Required Python packages: `re`, `collections`

### Setup

1. **Clone the Repository**

   Clone the repository to your local machine:

   ```sh
   git clone https://github.com/YourUsername/YourRepository.git
   ```

2. **Navigate to the Directory**

   Change to the directory where the script is located:

   ```sh
   cd YourRepository
   ```

3. **Install Required Packages**

   Ensure you have the required Python packages installed. The script uses built-in Python libraries, so no additional installation is needed.

### Usage

1. **Prepare the Log File**

   Create a file named `access.log` in the same directory as the script. Ensure it contains sample log entries, for example:

   ```plaintext
   127.0.0.1 - - [22/Jul/2024:00:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024
   127.0.0.1 - - [22/Jul/2024:00:00:01 +0000] "GET /about.html HTTP/1.1" 200 2048
   127.0.0.1 - - [22/Jul/2024:00:00:02 +0000] "GET /contact.html HTTP/1.1" 404 512
   192.168.0.1 - - [22/Jul/2024:00:00:03 +0000] "GET /index.html HTTP/1.1" 200 1024
   ```

2. **Run the Script**

   Execute the script using Python:

   ```sh
   python backup_solution.py
   ```

3. **View Output**

   The script will print the following information to the console:

   - Number of 404 Errors
   - Most Requested Pages
   - Most Frequent IP Addresses

### Example Output

```plaintext
Number of 404 Errors: 2
Most Requested Pages:
/index.html: 3
/about.html: 2
/contact.html: 1
Most Frequent IPs:
127.0.0.1: 4
192.168.0.1: 2
```

### Troubleshooting

- **FileNotFoundError:** Ensure that `access.log` exists in the same directory as the script and is named correctly.
- **Deprecation Warnings:** If you encounter deprecation warnings, consider updating your libraries or suppressing the warnings temporarily.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

You can copy this content and save it as `README.md` in your project directory. Let me know if you need any more adjustments!
