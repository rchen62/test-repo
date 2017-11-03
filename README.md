# py27-spyder

* Source code - [Gitlab][10]

[10]: https://gitlab.fngn.com/bi/py27-spyder

## About

This project demonstrates how to use Python 2.7 with the Spyder IDE.

## Setup the project

### Install pre-requisites

1. [Git bash][20]

[20]: https://git-for-windows.github.io/

2. [Miniconda 64-bit exe installer. Python 3.6][30]

[30]: https://conda.io/miniconda.html

### Clone the project

1. Display your ssh keys

    ```
    dir %USERPROFILE%\.ssh
    ```

2. If you do not have keys type the following and select the defaults
Press `Enter` for all options. Typically (c:\Program Files\Git\usr\bin\ssh-keygen.exe)

    ```
    ssh-keygen
    ```

3. Login to [Gitlab][40]

[40]: https://gitlab.fngn.com/users/sign_in

4. Add an [SSH key][50] to Gitlab

[50]: https://gitlab.fngn.com/profile/keys

5. Get the project from Gitlab

    ```
    git clone git@gitlab.fngn.com:bi/py27-spyder.git
    ```

### Create an environment from a file

1. Change to the root directory of the project

    ```
    cd py27-spyder
    ```

2. Display existing environments

    ```
    conda env list
    ```

3. Create the dbutil environment if it does not exist

    ```
    conda env create -f environment.yml
    ```

4. Activate the environment

    ```
    activate py27
    ```

5. Run Spyder

    ```
    spyder
    ```

6. Deactivate the environment

    ```
    deactivate
    ```

### Create an environment by specifying libraries (optional)

1. Run the script below for Windows

    ```
    conda create -n py27 python=2.7
    activate py27
    conda install -y spyder
    conda install -y numpy
    conda install -y pandas
    conda install -y pytest
    conda install -y yapf
    conda env export --file environment.yml
    deactivate
    ```

## Videos on learning Python 2.7 with Spyder

1. [Python With Spyder 1: First Steps (Updated 7/24/2015)][100] - Start at 10:00 minutes

[100]: https://www.youtube.com/watch?v=J5GevIHNctM

2. [Python With Spyder 2: Basic Arithmetic and Variable Assignment][110]

[110]: https://www.youtube.com/watch?v=OPuDjdRjtyY

3. [Python With Spyder 3: Functions and Scoping][120]

[120]: https://www.youtube.com/watch?v=GT1UfkLIeZ4

4. [Python With Spyder 4: Strings, Indexing, and Slicing][130]

[130]: https://www.youtube.com/watch?v=OKelK8-NGg8

5. [Python With Spyder 5: Lists Part 1][140]

[140]: https://www.youtube.com/watch?v=1qeKsuhww8g

6. [Python With Spyder 6: Lists Part 2][150]

[150]: https://www.youtube.com/watch?v=Ghb4wMW0YX4

7. [Python With Spyder 7: The Idea of Objects (Updated 7/16/15)][160]

[160]: https://www.youtube.com/watch?v=G6U5fQ8Siwo

8. [Python With Spyder 8: Python Objects Part 1 (Revised 7/17/2015)][170]

[170]: https://www.youtube.com/watch?v=JJPM7hI4fjE

9. [Python With Spyder 9: Objects Part 2 - Attributes and Methods and a Few Spyder "Tricks"][180]

[180]: https://www.youtube.com/watch?v=oj4bWBFptt4

10. [Python With Spyder 10: Objects Part 3 - Private Data and Encapsulation][190]

[190]: https://www.youtube.com/watch?v=VstfQaQjSBc

11. [Python With Spyder 11: Objects Part 4 -- Inheritance][200]

[200]: https://www.youtube.com/watch?v=ueDdQ8sx6SM

12. [Python With Spyder 12: Dictionaries][210]

[210]: https://www.youtube.com/watch?v=FzzYUbSuOSU

13. [Python With Spyder 13: For Loops][220]

[220]: https://www.youtube.com/watch?v=w7sfSkQqdgw

14. [Python With Spyder 14: If Statements][230]

[230]: https://www.youtube.com/watch?v=1bDSv18zGTU

## Miscellaneous

Excellent video on introduction to Pandas
https://www.youtube.com/watch?v=dye7rDktJ2E

git clone https://github.com/chendaniely/2016-pydata-carolinas-pandas

Data Analysis with Python and Pandas Tutorial Introduction

https://pythonprogramming.net/data-analysis-python-pandas-tutorial-introduction/

pip install pandas_datareader
import pandas_datareader.data as web

