# python-bdd-behave

Example python bdd project using behave for this [blog post](http://www.shdavidson.com/2015/09/03/python-bdd-behave/).

## setup

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
BROWSER  | firefox
ENV  | production
