# IBM Globalization Automation Tool

An automation Python tool built with the Selenium WebDriver module, to automate the IBM Globalization checking process, checking for all the the globalization checklist items one by one, currently working on Chrome 72 (Chromedriver 2.46)

### How does it work?

It receives a list of pages, and then uses the WebDriver Selenium tool to check all the pages according to the IBM Globalization Standards, and creates a .txt file for each of those pages with the issues report

### Instalation

For this tool to work, you should have Python 27, Selenium and Chromedriver installed in your machine, after you make sure you have them installed, download all the repo files and execute the 'globalization-automation.py' file

### Browser Support:

* Google Chrome 72+

### Built with:

* [Python](https://www.python.org/)
* [Selenium](https://github.com/SeleniumHQ/selenium)
* [Chromedriver](http://chromedriver.chromium.org)

### Source and Reference links:

* [IBM Globalization Checklist](https://ibm.ent.box.com/notes/293916499560?s=xlh67zuqbqlqjdtd62e9u2a9bo4zhj5w) - The checklist used as a base to create the Globalization Automation tool
* [IBM Northstar Standards (V18)](https://www.ibm.com/standards/web/v18/design/) - The general standards for building all pages
