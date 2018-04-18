"""Provides some utilities widely used by other modules"""

import bisect
import collections
import collections.abc
import operator
import os.path
import random
import math
import functools
from itertools import chain, combinations


# ______________________________________________________________________________
# Functions on Sequences and Iterables


def sequence(iterable):
    """Coerce iterable to sequence, if it is not already one."""
    return (iterable if isinstance(iterable, collections.abc.Sequence)
            else tuple(iterable))


def removeall(item, seq):
    """Return a copy of seq (or string) with all occurences of item removed."""
    if isinstance(seq, str):
        return seq.replace(item, '')
    else:
        return [x for x in seq if x != item]


def unique(seq):  # TODO: replace with set
    """Remove duplicate elements from seq. Assumes hashable elements."""
    return list(set(seq))


def count(seq):
    """Count the number of items in sequence that are interpreted as true."""
    return sum(bool(x) for x in seq)


def product(numbers):
    """Return the product of the numbers, e.g. product([2, 3, 10]) == 60"""
    result = 1
    for x in numbers:
        result *= x
    return result


def first(iterable, default=None):
    """Return the first element of an iterable or the next element of a generator; or default."""
    try:
        return iterable[0]
    except IndexError:
        return default
    except TypeError:
        return next(iterable, default)


def is_in(elt, seq):
    """Similar to (elt in seq), but compares with 'is', not '=='."""
    return any(x is elt for x in seq)


def mode(data):
    """Return the most common data item. If there are ties, return any one of them."""
    [(item, count)] = collections.Counter(data).most_common(1)
    return item


def powerset(iterable):
    """powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))[1:]


# ______________________________________________________________________________
# argmin and argmax


identity = lambda x: x

argmin = min
argmax = max


def argmin_random_tie(seq, key=identity):
    """Return a minimum element of seq; break ties at random."""
    return argmin(shuffled(seq), key=key)


def argmax_random_tie(seq, key=identity):
    """Return an element with highest fn(seq[i]) score; break ties at random."""
    return argmax(shuffled(seq), key=key)


def shuffled(iterable):
    """Randomly shuffle a copy of iterable."""
    items = list(iterable)
    random.shuffle(items)
    return items


# ______________________________________________________________________________
# Statistical and mathematical functions


def histogram(values, mode=0, bin_function=None):
    """Return a list of (value, count) pairs, summarizing the input values.
    Sorted by increasing value, or if mode=1, by decreasing count.
    If bin_function is given, map it over values first."""
    if bin_function:
        values = map(bin_function, values)

    bins = {}
    for val in values:
        bins[val] = bins.get(val, 0) + 1

    if mode:
        return sorted(list(bins.items()), key=lambda x: (x[1], x[0]),
                      reverse=True)
    else:
        return sorted(bins.items())


def dotproduct(X, Y):
    """Return the sum of the element-wise product of vectors X and Y."""
    return sum(x * y for x, y in zip(X, Y))


def element_wise_product(X, Y):
    """Return vector as an element-wise product of vectors X and Y"""
    assert len(X) == len(Y)
    return [x * y for x, y in zip(X, Y)]


def matrix_multiplication(X_M, *Y_M):
    """Return a matrix as a matrix-multiplication of X_M and arbitary number of matrices *Y_M"""

    def _mat_mult(X_M, Y_M):
        """Return a matrix as a matrix-multiplication of two matrices X_M and Y_M
        >>> matrix_multiplication([[1, 2, 3],
                                   [2, 3, 4]],
                                   [[3, 4],
                                    [1, 2],
                                    [1, 0]])
        [[8, 8],[13, 14]]
        """
        assert len(X_M[0]) == len(Y_M)

        result = [[0 for i in range(len(Y_M[0]))] for j in range(len(X_M))]
        for i in range(len(X_M)):
            for j in range(len(Y_M[0])):
                for k in range(len(Y_M)):
                    result[i][j] += X_M[i][k] * Y_M[k][j]
        return result

    result = X_M
    for Y in Y_M:
        result = _mat_mult(result, Y)

    return result


def vector_to_diagonal(v):
    """Converts a vector to a diagonal matrix with vector elements
    as the diagonal elements of the matrix"""
    diag_matrix = [[0 for i in range(len(v))] for j in range(len(v))]
    for i in range(len(v)):
        diag_matrix[i][i] = v[i]

    return diag_matrix


def vector_add(a, b):
    """Component-wise addition of two vectors."""
    return tuple(map(operator.add, a, b))


def scalar_vector_product(X, Y):
    """Return vector as a product of a scalar and a vector"""
    return [X * y for y in Y]


def scalar_matrix_product(X, Y):
    """Return matrix as a product of a scalar and a matrix"""
    return [scalar_vector_product(X, y) for y in Y]


def inverse_matrix(X):
    """Inverse a given square matrix of size 2x2"""
    assert len(X) == 2
    assert len(X[0]) == 2
    det = X[0][0] * X[1][1] - X[0][1] * X[1][0]
    assert det != 0
    inv_mat = scalar_matrix_product(1.0/det, [[X[1][1], -X[0][1]], [-X[1][0], X[0][0]]])

    return inv_mat


def probability(p):
    """Return true with probability p."""
    return p > random.uniform(0.0, 1.0)


def weighted_sample_with_replacement(n, seq, weights):
    """Pick n samples from seq at random, with replacement, with the
    probability of each element in proportion to its corresponding
    weight."""
    sample = weighted_sampler(seq, weights)

    return [sample() for _ in range(n)]


def weighted_sampler(seq, weights):
    """Return a random-sample function that picks from seq weighted by weights."""
    totals = []
    for w in weights:
        totals.append(w + totals[-1] if totals else w)

    return lambda: seq[bisect.bisect(totals, random.uniform(0, totals[-1]))]


def rounder(numbers, d=4):
    """Round a single number, or sequence of numbers, to d decimal places."""
    if isinstance(numbers, (int, float)):
        return round(numbers, d)
    else:
        constructor = type(numbers)     # Can be list, set, tuple, etc.
        return constructor(rounder(n, d) for n in numbers)


def num_or_str(x):
    """The argument is a string; convert to a number if
       possible, or strip it."""
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError:
            return str(x).strip()


def normalize(dist):
    """Multiply each number by a constant such that the sum is 1.0"""
    if isinstance(dist, dict):
        total = sum(dist.values())
        for key in dist:
            dist[key] = dist[key] / total
            assert 0 <= dist[key] <= 1, "Probabilities must be between 0 and 1."
        return dist
    total = sum(dist)
    return [(n / total) for n in dist]


def norm(X, n=2):
    """Return the n-norm of vector X"""
    return sum([x**n for x in X])**(1/n)


def clip(x, lowest, highest):
    """Return x clipped to the range [lowest..highest]."""
    return max(lowest, min(x, highest))


def sigmoid_derivative(value):
    return value * (1 - value)


def sigmoid(x):
    """Return activation value of x with sigmoid function"""
    return 1/(1 + math.exp(-x))


def step(x):
    """Return activation value of x with sign function"""
    return 1 if x >= 0 else 0


def gaussian(mean, st_dev, x):
    """Given the mean and standard deviation of a distribution, it returns the probability of x."""
    return 1/(math.sqrt(2*math.pi)*st_dev)*math.e**(-0.5*(float(x-mean)/st_dev)**2)


try:  # math.isclose was added in Python 3.5; but we might be in 3.4
    from math import isclose
except ImportError:
    def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
        """Return true if numbers a and b are close to each other."""