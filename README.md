# Personal Utility Functions

This repository contains personal utility functions that I use frequently in my projects. The functions are written in Python and are designed to be reusable and easy to integrate into any project.

## Available Utils

### SortingHat

The SortingHat Class contains the following algorithms.
* `insertion_sort`:  0(n^2) Takes an array of integer or floating point numbers sorts in ascending or descending order.

## Installation
Navigate to your project folder:
```bash
cd /home/user/myproject
git clone https://github.com/MayorDobe/fisher-untils.git
cd fisher-utils
pip install -e .
```
### Example
```python
import utils.sorters.sorting_hat as sh

if __name__ == "__main__":
    list_sorter: sh.SortingHat = sh.SortingHat()
    random_array: list[int] = [6, 10, 3, 9, 5, 1, 7, 8, 4, 2]
    list_sorter.insertion_sort(array=random_array, length=len(random_array))
    print(random_array)
```
Output:
```bash
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
