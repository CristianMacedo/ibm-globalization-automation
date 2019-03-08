# IBM Globalization Automation Tool

An automation Python tool built with the Selenium WebDriver module, to automate the IBM Globalization checking process, checking for all the the globalization checklist items one by one, currently working on Chrome 72 (Chromedriver 2.46)

## How does it work?

It receives a list of pages, and then uses the WebDriver Selenium tool to check all the pages according to the IBM Globalization Standards, and creates a .txt file for each of those pages with the issues report

## Support:

* Google Chrome 72
* Mac OS 10.10+

## What programs/modules do I need?

For this tool to work you will need the following Programs and Modules installed

* [Python 3](https://www.python.org/)
  * [Requests 2.19.1](https://pypi.org/project/requests) (Installing instructions below)
  * [Selenium 3.141.0](https://pypi.org/project/selenium/) (Installing instructions below)
* [Google Chrome 72 - Mac OS X 10.10+](https://www.google.com/chrome/)

## Installation

After having Python 3 and Google Chrome installed

1. Install 'Selenium' and 'Requests' Python modules:

```sh
pip3 install selenium
pip3 install requests
```

1. Download 'globalization-automation.py' file and 'chromedriver' unix executable from the repo
1. Open the 'globalization-automation.py' file and replace the CHROMEDRIVER_PATH and CHROME_PROFILE_PATH variables values:
   1. CHROMEDRIVER_PATH: Replace with the 'chromedriver' downloaded file path
   1. CHROME_PROFILE_PATH: Replace with your Chrome Profile path *(See how to find your Chrome Profile path below)

### Findind your Chrome Profile path

Selenium WebDriver opens a raw new instance of google chrome, which doesn't load any login cached data, that's why we need to use a saved profile to be able to save Drupal login data

1. Search for 'chrome://version/' on you Chrome Browser 
   
   <img width="300" align="middle" alt="chrome version search" src="https://user-images.githubusercontent.com/37914402/53930473-230bc700-4070-11e9-8333-db1e0293d389.png">
   
1. Find the 'Profile Path' field 
   
   <img width="500" align="middle" alt="chrome version page" src="https://user-images.githubusercontent.com/37914402/53930752-3ec39d00-4071-11e9-83d2-e2ce02d61cc2.png">

## Usage

On the 'globalization-automation.py' file, add the Node URLs to the 'pages' list, on quotation marks, and separed with commas. (Currently works only with node links ('https://cms.ibm.com/node/*')
> I'm still implementing an interactive input so the user doesn't need to manually add the URLs and paths

```python
...
# List of pages to check. WORKS ONLY WITH NODE LINKS
pages = ['https://cms.ibm.com/node/1208921']

for url in pages:
startCheck(url)
```

## Source and Reference links:

* [IBM Globalization Checklist](https://ibm.ent.box.com/notes/293916499560?s=xlh67zuqbqlqjdtd62e9u2a9bo4zhj5w) - The checklist used as a base to create the Globalization Automation tool
* [IBM Northstar Standards (v18)](https://www.ibm.com/standards/web/v18/design/) - The general standards for building all pages

License
----

IBM
