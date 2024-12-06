# OSINT-Automation-Tool
A simple yet powerful Python-based tool with a graphical user interface (GUI) to automate Open Source Intelligence (OSINT) gathering for a target domain. This tool leverages popular libraries and public APIs to provide critical information about a domain, including WHOIS details, IP address, geolocation, and subdomains.

**Features**
* WHOIS Lookup: Fetch domain registrar, creation date, and expiration date.
* IP Address Resolution: Identify the IP address of the target domain.
* Geolocation: Retrieve geographical details of the domain's IP address.
* Subdomain Enumeration: Discover subdomains using the HackerTarget API.
* User-Friendly GUI: Built with tkinter for easy input and clear output.

**How to Use**
1. Clone the repository:

   git clone https://github.com/iamnalaemton/osint-automation-tool.git
   
   cd osint-automation-tool
   
2. Install dependencies:

   pip install requests python-whois shodan
   
3. Run the tool:

   python osint_tool.py
   
4. Enter the target domain in the input field and click 'Start OSINT'. The results will appear in the output section.

**Screenshot**

![image](https://github.com/user-attachments/assets/6a355d64-af91-4786-a166-86cac671fbd4)

**Requirements**
* Python 3.6 or higher
* Dependencies: requests, python-whois, shodan

**Future Enhancements**
1. Add support for DNS record fetching and SSL certificate analysis.
2. Integrate APIs like Shodan and VirusTotal for deeper analysis.
3. Export results as a report (e.g., CSV or PDF).

**Contribution**

Contributions are welcome! If you have ideas for improvements or new features, feel free to fork the repository, make changes, and submit a pull request.

**License**

This project is licensed under the MIT License. See the LICENSE file for details.
