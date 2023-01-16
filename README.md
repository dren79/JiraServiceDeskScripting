# JiraServiceDeskScripting

This repo is being made available as is, minimal tidy-up has been done, I will continue to support and refactor as time allows (pull requests welcome).

This is code I have used to create hundreds of Jira tickets in minutes saving hours/days of Jira Donkey work.

Refactors, updates, additions and new ways of using this would be greatly appreciated, please consider contributing. 

## What is this repository for? ##

* Quick summary:
  * Automating Jira Servicedesk issue creation


### Usecases ###

* Requested at an Atlassian meetup


## How do I get set up? ##
* Normal Python 3.10 or higher setup should be followed, download Python here - https://www.python.org/downloads/.
  * A virtual environment should be set up `python -m venv .`
  * Activate the virtual environment `source venv/bin/activate` (this may be different on your system, check the created venv folder to ensure the path to the activate.py file is the same)
  * Install the imported packages `pip install -r requirements.txt` (this may be different on your system depending on the pip alias)
* Set up a free instance of Jira Cloud `https://www.atlassian.com/software/jira/free`
* This demo was set up with one free servicedesk instance 'service_test' with the key ST.
* Create a copy of the .env_template file and name it `.env` exactly
* Fill out the necessary fields in the newly created .env file (BASE_URL should look like this - https://YOURPROJECT.atlassian.net)
* Your API token can be created by: 
  1. logging into Jira Cloud (the one you created earlier)
  2. Click on your avatar in the top right
  3. Click Account Settings
  4. Navigate to the Security tab on the left
  5. Click Create and manage API tokens
* If creating stories from a CSV file, place it in the inputs folder to avoid sensitive data being committed to the repo.
* If creating a report output file (Json files are outputted by some scripts), please put it in the reports folder to avoid sensitive data being committed to the repo.


### Contribution guidelines ###

* Please contribute frequently and openly!

### References ###
* Expansion - https://docs.atlassian.com/jira-servicedesk/REST/3.6.2/#expansion
* Service Desk API home page - https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/

### Who do I talk to? ###

* Original Creator - David Renton david.renton@genesys.com
