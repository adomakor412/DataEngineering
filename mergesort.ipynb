{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Lab and Homework 1: Introduction to Algorithms\n",
    "\n",
    "**In class**: *Thursday, February 6, 2020*  \n",
    "**Homework Due** : *5 PM, Thursday, February 13, 2020*\n",
    "\n",
    "# Learning Goals\n",
    "\n",
    "Data Engineering is the hardware and software infrastructure for doing Data Science at scale. Netflix processes over one trillion events a day. Their data warehouse is about 100 *petabytes*. Amazon's product database has in exccess of 600 million items. We'll study many of the technologies that underpin data engineering--databases, stream processing, map reduce, etc. To do this, we'll need an intuitive understanding of scale and a conceptual framework for how scale impacts our ability to process massive amounts of data. \n",
    "\n",
    "What makes for a \"good\" program or algorithm? What metrics does one use to assess an algorithm? \n",
    "\n",
    "These are the questions we'll explore in this lab. Many of the topics we'll cover in this course (e.g., database indexing) require a conceptual framework and associated terminology to properly grasp. The ideas we develop here will help you underst\n",
    "\n",
    "As with all the subjects we'll study, we won't begin to scratch the surface of this subject. For further illucidation, Tim Roughgarden's three volume series [_Algorithms Illuminated_](https://www.amazon.com/Algorithms-Illuminated-Part-1-Basics/dp/0999282905/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=1580852108&sr=8-1-spons) is highly recommended. Get the first volume, put it on your nightstand, read a handful of pages before bedtime. You'll be richly rewarded by the end of the semester.\n",
    "\n",
    "This lab is intended for the three quarters of the students who have not studied Computer Science formally. Those who did will be bored to tears. Feel free to skim.\n",
    "\n",
    "# Teaching Approach\n",
    "\n",
    "We roughly follow Aristotle's method of teaching in this course. Instead of explaining principles first and then testing your understanding with problems, we'll often start with a series of leading questions. By grappling with these questions you will intuit and induce the concepts being taught. Questions first, principles, terminology and notation later.\n",
    "\n",
    "\n",
    "# Searching\n",
    "\n",
    "## Problem 1: Searching an array\n",
    "Consider the following Python array. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = [3, 1, 5, 2, 4, 9, 8, 7, 6, 10]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Write a function `search_array`, which takes a Python list (aka array) two arguments a list `lst` to search and a value `v` to find. `search_array` returns the index of the element if the element exists in the array and `-1` if the element cannot be found. \n",
    "\n",
    "Don't be clever! Implement the first and most obvious thing that comes to mind.\n",
    "\n",
    "Here's a template for the function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "metadata": {},
   "outputs": [],
   "source": [
    "def search_array(lst, v):\n",
    "    index = -1\n",
    "    if v in lst:\n",
    "        index = lst.index(v)\n",
    "    return index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 164,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "search_array(a,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 165,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "search_array(a,0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "nteract": {
     "transient": {
      "deleting": false
     }
    }
   },
   "source": [
    "## Unit Test for Linear Search"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "test_found (__main__.TestArraySearch) ... ok\n",
      "test_not_found (__main__.TestArraySearch) ... ok\n",
      "\n",
      "----------------------------------------------------------------------\n",
      "Ran 2 tests in 0.017s\n",
      "\n",
      "OK\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<unittest.main.TestProgram at 0x10dacbd60>"
      ]
     },
     "execution_count": 166,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import unittest\n",
    "\n",
    "class TestArraySearch(unittest.TestCase):\n",
    "\n",
    "    def test_found(self):\n",
    "        self.assertEqual(search_array(a, 2), 3)\n",
    "        \n",
    "    def test_not_found(self):\n",
    "        self.assertEqual(search_array(a, 11), -1)\n",
    "\n",
    "# Run the unit tests          \n",
    "unittest.main(defaultTest=\"TestArraySearch\", argv=['ignored', '-v'], exit=False)\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "The program you just wrote was probably ($P > 0.99$!) _linear_ or _sequential_ search. You scanned the list until you found the first occurence of the search term, or, having reached the end returned `-1`.\n",
    "\n",
    "Linear search is a perfectly good algorithm. It's simple, it gets the job done. In many cases, it's exactly what you want. For searching a web page or a deck of cards it will do nicely.\n",
    "\n",
    "But what if you looking for one of the 600 million products on Amazon's store. Would your design suffice? Let's examine that question with three more:\n",
    "\n",
    "## Problem 2: Analyzing the Search Function\n",
    "\n",
    "1. What's the **best** case scenario for linear search?\n",
    "2. What is the **worst** case?\n",
    "3. What is the **average** case?\n",
    "\n",
    "The answers to the first two questions are obvious, the last one less so. Here's how to think about it.\n",
    "\n",
    "Assume that it's equally probable that the search term is located at any of the $n$ array slots. So the search term is _uniformly_ distributed with the probability of it being found at any particular index being $1/n$. You want to compute the _Expected_ value $E$ of the random variable $X$ where $X$ can take on values $0..n-1$ with respective probabilities $p(0), p(1), ... p(n-1) = 1/n$:\n",
    "\n",
    "$$\n",
    "E[X] = \\sum_{j=1}^N p(j) j\n",
    "$$\n",
    "\n",
    "Expand the above expression into a closed form to compute $E[X]$. Hint: look for the arithmetic series.\n",
    "\n",
    "With the above analysis in hand, would you recommend linear search for Amazon's product database? Assuming it takes $100$ microseconds to iterate over each array element, how long would it take on average to search Amazon's 600 million product records? (We're grossly simplifying by ignoring memory load times and other important details.)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "nteract": {
     "transient": {
      "deleting": false
     }
    }
   },
   "source": [
    "## Problem 3:\n",
    "\n",
    "Can we improve upon linear search? Sure, if we can make assumptions about the data. For example, the data might already be **sorted**. To see how a sorted list might help, consider the following questions:\n",
    "\n",
    "1. What is the _median_ element of a sorted list or array? (Think about the definition of medan: the value that separates the lower half of values in the list from the upper half.)\n",
    "2. How does knowing the median element help narrow the search space and by how much?\n",
    "3. Having narrowed the space by using the median, could you do it again _recursively_.\n",
    "\n",
    "In answering the above questions it might help to work with a real list like this one:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false,
     "source_hidden": false
    },
    "nteract": {
     "transient": {
      "deleting": false
     }
    }
   },
   "outputs": [],
   "source": [
    "sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]\n",
    "\n",
    "# How would you find the element 14 using the approach hinted at above?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "nteract": {
     "transient": {
      "deleting": false
     }
    }
   },
   "source": [
    "Armed with answers to the above questions, write a function called `binary_search` which will do the same thing as the linear `search_array` function you wrote above, except it will take an already sorted array as an argument, compare the search term with the median, and recurse down the left or right sides of the array depending on whether the search term is less than or greater than the median."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false,
     "source_hidden": false
    },
    "nteract": {
     "transient": {
      "deleting": false
     }
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' med = round(statistics.median(a))\\n    candidate = a[med]\\n    if term == candidate:\\n        found = med\\n    else:\\n        while term != candidate:\\n            a_prime = a[:round(len(a)/2)]\\n            if len(a_prime) == len(a):\\n                break\\n            binary_search(a_prime,term,len(a))\\n        \\n    return found\\n'"
      ]
     },
     "execution_count": 169,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "def binary_search(a, term, length):\n",
    "    \"\"\"\n",
    "    Search a sorted array.\n",
    "    \n",
    "    Parameters:\n",
    "    a (array): Array to search\n",
    "    term: What to search for\n",
    "    length (int): Size of the list\n",
    "    \n",
    "    Returns:\n",
    "    int: index of term if found, -1 otherwise\n",
    "    \"\"\"\n",
    "    left = 0\n",
    "    right = length - 1\n",
    "    found = -1\n",
    "    \n",
    "    while left <= right:#compare indices\n",
    "        med = math.floor((left+right)/2)\n",
    "        if term == a[med]:\n",
    "            return med  \n",
    "        elif term < a[med]:\n",
    "            right = med-1\n",
    "        else:\n",
    "            left = med+1\n",
    "        #length = right - left +1\n",
    "    \n",
    "    return found\n",
    "\n",
    "''' med = round(statistics.median(a))\n",
    "    candidate = a[med]\n",
    "    if term == candidate:\n",
    "        found = med\n",
    "    else:\n",
    "        while term != candidate:\n",
    "            a_prime = a[:round(len(a)/2)]\n",
    "            if len(a_prime) == len(a):\n",
    "                break\n",
    "            binary_search(a_prime,term,len(a))\n",
    "        \n",
    "    return found\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 170,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a= range(10)\n",
    "b = 20\n",
    "c = len(a)\n",
    "\n",
    "binary_search(a,b,c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false,
     "source_hidden": false
    },
    "nteract": {
     "transient": {
      "deleting": false
     }
    }
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "test_found (__main__.TestBinarySearch) ... ok\n",
      "test_not_found (__main__.TestBinarySearch) ... "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[13 22 29 37 67 73 84 92 92 93 94]\n",
      "[ 8 12 41 44 65 68 85 90 91 93]\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ok\n",
      "\n",
      "----------------------------------------------------------------------\n",
      "Ran 2 tests in 0.085s\n",
      "\n",
      "OK\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<unittest.main.TestProgram at 0x10db54d60>"
      ]
     },
     "execution_count": 171,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import unittest\n",
    "\n",
    "class TestBinarySearch(unittest.TestCase):\n",
    "\n",
    "    def test_found(self):\n",
    "        a = np.sort(np.append(np.random.randint(0, 100, 10), 73))\n",
    "        print(a)\n",
    "        i = binary_search(a, 73, len(a))\n",
    "        self.assertEqual(a[i], 73)\n",
    "        \n",
    "    def test_not_found(self):\n",
    "        a = np.sort(np.random.randint(0, 100, 10))\n",
    "        print(a)\n",
    "        self.assertEqual(binary_search(a, 101, len(a)), -1)\n",
    "\n",
    "# Run the unit tests          \n",
    "unittest.main(defaultTest=\"TestBinarySearch\", argv=['ignored', '-v'], exit=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "nteract": {
     "transient": {
      "deleting": false
     }
    }
   },
   "source": [
    "## Problem: Analyzing Binary Search\n",
    "\n",
    "What are the best case, worst case, and average case running times for `binary_search` as a function of the length of the input array?\n",
    "\n",
    "Assuming all of Amazon's 600 million product IDs could be loaded into a sorted array (they are not ever in practice), who many steps on average and at worst, would it take to find a product?\n",
    "\n",
    "We have just uncovered a class of algorithm called _Divide-and-Conquer_, a fundamental algorithmic technique that has many applications, including to sorting, our next subject.\n",
    "\n",
    "# Sorting\n",
    "\n",
    "So `binary_search` dramatically improves over `linear_search`. But how expensive is it to sort? This is the subject we explore now. It turns out that there are fundamental limits to sorting. That is, no algorithm can be devised to exceed the theoretic bound. (We will derive the bound in this course; see an Algorithms book for details.)\n",
    "\n",
    "In what follows, we'll develop two sorting algorithms: the first a simple and obvious approach called `selection_sort`, the second, called `merge_sort` applies the divide-and-conquer strategy to sorting. \n",
    "\n",
    "## Problem: Selection Sort\n",
    "\n",
    "Selection Sort and it's sibling Insertion Sort are obvious sorting algorithms. You have depended on one or the other whenever you sort a hand of playing cards. \n",
    "\n",
    "In both approaches, you split the hand into two parts: sorted and unsorted.\n",
    "\n",
    "With selection sort you stort by finding the minimum in your unsorted hand. Place that card on the left and keep the unsorted cards to the right. Now scan the unsorted side for the next minimum and move the card to the end of the sorted side. \n",
    "\n",
    "When you implement `selection_sort` on a computer you don't maintain two separate arrays for sorted and unsorted. Instead, you sort the array _in place_. \n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false,
     "source_hidden": false
    },
    "nteract": {
     "transient": {
      "deleting": false
     }
    }
   },
   "outputs": [],
   "source": [
    "# Implement Selection Sort\n",
    "\n",
    "def selection_sort(a):\n",
    "    myList = list(a)\n",
    "    for i in range(len(a)):\n",
    "        small = min(myList[i:]) #O(nlog(n))\n",
    "        myList.remove(small)\n",
    "        myList.insert(i,small)\n",
    "    return myList    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false,
     "source_hidden": false
    },
    "nteract": {
     "transient": {
      "deleting": false
     }
    }
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "test_selection_sort (__main__.TestSelectionSort) ... "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[61  5 88 81 45 91 54 47 76 33]\n",
      "[5, 33, 45, 47, 54, 61, 76, 81, 88, 91]\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ok\n",
      "\n",
      "----------------------------------------------------------------------\n",
      "Ran 1 test in 0.009s\n",
      "\n",
      "OK\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<unittest.main.TestProgram at 0x10e946a00>"
      ]
     },
     "execution_count": 187,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import unittest\n",
    "\n",
    "class TestSelectionSort(unittest.TestCase):\n",
    "\n",
    "    def test_selection_sort(self):\n",
    "        a = np.random.randint(0, 100, 10)\n",
    "        print(a)\n",
    "        #selection_sort(a)\n",
    "        a = selection_sort(a) #correction to unit test\n",
    "        b = np.sort(np.array(a, copy=True))\n",
    "        self.assertSequenceEqual(list(a), list(b))\n",
    "        print(a)\n",
    "        \n",
    "\n",
    "# Run the unit tests          \n",
    "unittest.main(defaultTest=\"TestSelectionSort\", argv=['ignored', '-v'], exit=False)        \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "nteract": {
     "transient": {
      "deleting": false
     }
    }
   },
   "source": [
    "## Problem: Analyzing Selection Sort\n",
    "\n",
    "Analyze your implementation and give the best, worst and average running times for `selection_sort`.\n",
    "\n",
    "## Merge Sort\n",
    "\n",
    "Merge Sort is a Divide and Conquer algorithm invented by John von Neumann in 1945. Like `binary_search` above it splits the input array down the middle. It then recursively calls itself (`merge_sort`) on the left and right halves before merging the now sorted halves into a single sorted result. We will go over the operation of `merge_sort` in detail in class.\n",
    "\n",
    "The code below shows the recursive top level implementation of `merge_sort`. For homework you should complete the implementation of `merge`, which takes two sorted arrays and merges them into a single sorted array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false,
     "source_hidden": false
    },
    "nteract": {
     "transient": {
      "deleting": false
     }
    }
   },
   "outputs": [],
   "source": [
    "def merge_sort(array,*args):\n",
    "    if len(array)<2:\n",
    "        return array\n",
    "\n",
    "    m = len(array)//2\n",
    "    return merge(merge_sort(array[:m]), merge_sort(array[m:]))\n",
    "    \n",
    "def merge(a, b):\n",
    "    if len(a)* len(b)==0:\n",
    "        return a+b\n",
    "    small = list(a[0] < b[0] and a or b).pop(0)\n",
    "    return [small] + merge(a, b)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "nteract": {
     "transient": {
      "deleting": false
     }
    }
   },
   "source": [
    "### Unit Test for Merge Sort"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "jupyter": {
     "outputs_hidden": false,
     "source_hidden": false
    },
    "nteract": {
     "transient": {
      "deleting": false
     }
    }
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "test_merge_sort (__main__.TestMergeSort) ... "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[33 41 15 97 40  6 40 82 47 49]\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ERROR\n",
      "\n",
      "======================================================================\n",
      "ERROR: test_merge_sort (__main__.TestMergeSort)\n",
      "----------------------------------------------------------------------\n",
      "Traceback (most recent call last):\n",
      "  File \"<ipython-input-2-653d72c8e984>\", line 9, in test_merge_sort\n",
      "    merge_sort(a, 0, len(a) - 1)\n",
      "  File \"<ipython-input-1-8b4de94f2466>\", line 6, in merge_sort\n",
      "    return merge(merge_sort(array[:m]), merge_sort(array[m:]))\n",
      "  File \"<ipython-input-1-8b4de94f2466>\", line 6, in merge_sort\n",
      "    return merge(merge_sort(array[:m]), merge_sort(array[m:]))\n",
      "  File \"<ipython-input-1-8b4de94f2466>\", line 6, in merge_sort\n",
      "    return merge(merge_sort(array[:m]), merge_sort(array[m:]))\n",
      "  File \"<ipython-input-1-8b4de94f2466>\", line 12, in merge\n",
      "    return [small] + merge(a, b)\n",
      "  File \"<ipython-input-1-8b4de94f2466>\", line 12, in merge\n",
      "    return [small] + merge(a, b)\n",
      "  File \"<ipython-input-1-8b4de94f2466>\", line 12, in merge\n",
      "    return [small] + merge(a, b)\n",
      "  [Previous line repeated 2941 more times]\n",
      "  File \"<ipython-input-1-8b4de94f2466>\", line 9, in merge\n",
      "    if len(a)* len(b)==0:\n",
      "RecursionError: maximum recursion depth exceeded while calling a Python object\n",
      "\n",
      "----------------------------------------------------------------------\n",
      "Ran 1 test in 0.154s\n",
      "\n",
      "FAILED (errors=1)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<unittest.main.TestProgram at 0x10e8c0c70>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import unittest\n",
    "\n",
    "class TestMergeSort(unittest.TestCase):\n",
    "\n",
    "    def test_merge_sort(self):\n",
    "        a = np.random.randint(0, 100, 10)\n",
    "        print(a)\n",
    "        merge_sort(a, 0, len(a) - 1)\n",
    "        b = np.sort(np.array(a, copy=True))\n",
    "        self.assertSequenceEqual(list(a), list(b))\n",
    "        print(a)\n",
    "        \n",
    "\n",
    "# Run the unit tests          \n",
    "unittest.main(defaultTest=\"TestMergeSort\", argv=['ignored', '-v'], exit=False)        \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "nteract": {
     "transient": {
      "deleting": false
     }
    }
   },
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 462,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[27, 72, 68, 41, 13, 10, 41, 6, 32, 24]\n",
      "[6, 10, 13, 24, 27, 32, 41, 41, 68, 72]\n"
     ]
    }
   ],
   "source": [
    "def merge(a, b):\n",
    "\tif len(a)*len(b) == 0:\n",
    "\t\treturn a+b\n",
    "\n",
    "\tv = (a[0] < b[0] and a or b).pop(0)\n",
    "\treturn [v] + merge(a, b)\n",
    "\n",
    "def mergesort(lst):\n",
    "\tif len(lst) < 2:\n",
    "\t\treturn lst\n",
    "\n",
    "\tm = len(lst)//2\n",
    "\treturn merge(mergesort(lst[:m]), mergesort(lst[m:]))\n",
    "\n",
    "mlst = list(np.random.randint(0, 100, 10))\n",
    "print (mlst)\n",
    "sorted = mergesort(mlst)\n",
    "\n",
    "print (sorted)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.0"
  },
  "nteract": {
   "version": "0.21.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
