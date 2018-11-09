# python-bdd-behave
![Travis](https://travis-ci.org/StephenDavidson/python-bdd-behave.svg?branch=master)
[![Requirements Status](https://requires.io/github/StephenDavidson/python-bdd-behave/requirements.svg?branch=master)](https://requires.io/github/StephenDavidson/python-bdd-behave/requirements/?branch=master)

Example python bdd project using behave for this [blog post](http://www.shdavidson.com/2015/09/03/python-bdd-behave/).

## setup

Requires `python >= 3.0`

```shell
git clone git@github.com:StephenDavidson/python-bdd-behave.git
cd python-bdd-behave
pip install -r requirements.txt
```

## running tests
``` shell
behave # run all feature files
behave features/ # run all feature files in the given folder
behave features/search.feature # run the search.feature file only
```

## env variables
variable  | default value
------------- | -------------
BROWSER  | chrome
ENV  | production
