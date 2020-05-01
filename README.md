# README : Network IT Tools


**Author:** Elisa Warner  
**Date:** 04/30/2020  

### Contents:
1. Capture Web Traffic
2. Command-Line Automated Gmail Script

## 1. Capture Web Traffic

### Description:
This code is designed to report the websites being visited by your computer (both in the foreground and background), along with a frequency count for how many times they have been visited. The code works by tracking all incoming DNS responses and recording their corresponding domain names as well as the frequency with which the same request has come in.

Some possible uses for this code could be for tracking background processes, monitoring history, creating an adblock, and monitoring for bots.

### Requirements:
* This code only runs on a MacOS but can be tweaked to work in Linux. It is also designed primarily for a wireless connection, but can be changed to ethernet by changing `en0` in line 17 to `eth0`.  
* python 3.6  
* `tcpdump`: To install `tcpdump`, simply go to your terminal and type `brew install tcpdump`. If you are not familiar with homebrew, or your command throws an error due to not recognizing the command `brew`, please download brew from this website: https://brew.sh/  

### How to Run:
The code should run out of the box. Simply type `python network_test.py` in the terminal window. You will be prompted for your administrator password (which is required to run tcpdump). The program will listen forever for incoming packets until `Ctrl+C` is applied by the user. The console will then display the resulting websites visited in order of frequency. Two files will also be created: `history.txt`, which gives the raw packet information from the DNS server, and `history_concat.txt`, which contains only the domain names and their frequency of visitation.

### Note:
This code is designed only to capture packets that are passing only between your IP address and the DNS server. If you want to capture outside packets, you need to enable monitor mode on your laptop and in some cases use your laptop as the access point. Because I am not as familiar with these concepts, I written the code with only a single computer's traffic in mind.

## 2. Command Line Automated Gmail Script

### Description:
This is some very simple code that makes small adjustments to Gmail's API example code. It is designed for people who know little about APIs and just want the code to work. The function of this code is to run a one-line command in the Terminal and have regular emails sent out, such as for lab meetings.

The `config.py` file contains an email template that can be adjusted based on the situation.

### Requirements
* python 3.6  
* `google-api-python-client`  
* `google-auth-httplib2`  
* `google-auth-oauthlib`  
* A `credentials.json` file authorized by Google

In order to get the above packages and credentials, please visit https://developers.google.com/gmail/api/quickstart/python and follow steps 1 and 2.

## How to Run:
In the command line (Terminal), type the following:
`python send_email.py [EmailType] [Person1] [Person2]`
where `[EmailType]`, `[Person1]` and `[Person2]` are substitutions for the email template, first blank of the template, and second blank of the template.

For example, a code of this:
`python send_email.py breadth Beth Jerry`
would result in the following email:

    Hi all:

    As a reminder, we will have a lab meeting today at 12:30pm. Presenting today will be Beth and Jerry on a few journal papers.

    Our lab meeting link is here:
    https://umich.bluejeans.com/yourlink
    Kind Regards
