from collections import Counter
import sys
import os

def checkArgs():
    ''' Check that there is only one argument'''
    if len(sys.argv) != 2:
        print "Error: Number of arguments are wrong!"
        print "Usage: num_factors.py <s for serial, m for multiprocessing, i for IPython.parallel (only one can be used at once)>"
        sys.exit()

    return sys.argv[(len(sys.argv)-1)]

def factorize(n):
    '''Factorising the number given'''

    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors
        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            p += 2
        else:
            p += 1

def serial():
    '''Serially count the number of unique factors when factorising all numbers between 2 and 50000'''
    uniq_dict = {}
    
    for i in range (2,50001):
        factors = factorize(i)
        factor_count = Counter(factors)
        uniq_factors = len(factor_count)
    
        if (uniq_factors in uniq_dict.keys()):
            uniq_dict[uniq_factors]+=1
        else:
            uniq_dict[uniq_factors] = 1

    print uniq_dict


def multiprocess():
    '''Count the number of unique factors when factorising all numbers between 2 and 50000, using multiprocessing'''
    import multiprocessing

    pool = multiprocessing.Pool(processes=4)
    result = pool.map_async(factorize, range(2,50001))
    
    all_factors = result.get()

    get_dict(all_factors)


def ipython():
    '''Count the number of unique factors when factorising all numbers between 2 and 50000, using iPython.parallel'''
    from IPython.parallel import Client
 
    try:
        client = Client()
    except IOError:
        sys.exit("Error: Make sure to run 'ipcluster start -n 4' first")
        
    dview = client[:]
    all_factors = dview.map_sync(factorize, range(2,50001))
    get_dict(all_factors)


def get_dict(all_factors):
    '''Returns a dictionary with number of unique factors from a list of lists with factors for each number'''
    uniq_dict = {}

    for factors in all_factors:
        factor_count = Counter(factors)
        uniq_factors = len(factor_count)
   
        if (uniq_factors in uniq_dict.keys()):
            uniq_dict[uniq_factors]+=1
        else:
            uniq_dict[uniq_factors] = 1
        
    print uniq_dict

def chooseVariant(flag):
    '''Choose which variant to run dependent of the flag'''
    if (flag == 's'):
        serial()
    elif (flag == 'm'):
        multiprocess()
    elif (flag == 'i'):
        ipython()
    else:
        print "\nGiven argument (",flag,") is not supported!\n"
        print "Usage: num_factors.py <s for serial, m for multiprocessing, i for IPython.parallel (only one can be used at the time)>"
        sys.exit()

if __name__ == '__main__':
    flag = checkArgs()
    chooseVariant(flag)
