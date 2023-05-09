# Useinsuder UI Tests
This repository contains an automated test written in Python using PyTest and Selenium that covers the following scenario:

1. V    isit https://useinsider.com/ and check if the Insider home page is opened or not.
2. Select "More" menu in the navigation bar, select "Careers" and check if the Career page, its Locations, Teams, and Life at Insider blocks are opened or not.
3. Click "See All Teams", select Quality Assurance, click "See all QA jobs", filter jobs by Location - Istanbul, Turkey, and department - Quality Assurance, check the presence of the jobs list.
4. Check that all jobs' Position contains "Quality Assurance", Department contains "Quality Assurance", Location contains "Istanbul, Turkey", and "Apply Now" button.
5. Click "Apply Now" button and check that this action redirects us to Lever Application form page.

- Screenshot should be taken If test fails one of steps
- Test case should be able to run in Chrome and Firefox browsers and ensure
that the browser is parametrically changeable.
- Test code should fully meet POM requirements
## Getting Started
These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites
To run the tests, make sure you have the following software installed on your system:
- Python 3.7 or higher
- Poetry (Python dependency management tool)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/VinichenkoB/UseinsiderUITests.git

```
2. Navigate to the project directory:
```bash
cd UseinsiderUITests
```

3. Install the required packages using Poetry:
```bash
poetry install
```

## Running the Tests
To run the tests, execute the following command in the project directory:

Run all tests:
```bash
poetry run pytest
```
