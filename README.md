# BMIG_5003_BASIC_BAYES
A simple bayes application

## Install
1. Download: ```git clone https://github.com/zpeterg/bmig_5003_basic_bayes```
2. Setup environment: ```conda env create -f environment.yml```

## Run
1. ```conda activate bayes```
2. ```python cookie.py```

## Design
1. Assumptions:
    1. That we never know which bowl the cookie is taken from.
    2. That the best estimate when the cookie is removed is to subtract the proportional estimate from both bowls.
2. I adapted the Likelihood method to work off of the total numbers of cookies and calculate the ratio from them (eg., vanilla-count / (vanilla-count + chocolate-count)).
3. I added copied and adapted the Update() method (to UpdateAndRemove()) to make it subtract the cookie ratio from the bowl after it's normalized. 