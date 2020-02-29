# Endor
Building Deep Forest approximations for pre-trained neural networks


## Motivation
The architecture of a traditional deep neural network resembles a series of stacked
ensemble classifiers. A Deep Forest approximation of a neural network (which has been pre-trained trained with gradient descent methods) can improve interpretability by providing insight into feature significance at each layer. 


## Dependency Management
Python packages are managed with <a href="https://pypi.org/project/pipenv/">pipenv</a>

To install dependencies, run
```
pipenv install
```

To begin a session, run
```
pipenv shell
``` 