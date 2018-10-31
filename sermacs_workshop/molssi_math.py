"""
molssi_math.py
Mean function of list

Calculates the mean of a list of numbers
"""


def mean(num_list):
    """
    Computes the mean of a list.

    Parameters
    ----------
    num_list: list
      List to calculate the mean of

    Returns
    -------
    mean: float
       Mean of list of numbers
    """

    list_mean = sum(num_list)/len(num_list)

    return list_mean

