#
# Issues:
#       1. There are two 'Dallas's in the cities list!
#          - There are Dallas' in Oregon and Texas.
#          - Most likely not only case of duplicates.
#
#       2. 'Panama' and 'Panama City' are matching the
#           Panama City headline!
#           - Consider longest match when both city and
#             country have matches. The ass-u-mtion is that
#             both country and city don't appear in same headline.
#
#=============================================================================

import re
import geonamescache
from unidecode import unidecode

def name_pat_fun(v):
    return f"\\b{v}\\b"

def gen_re_arr(names, pf):
    return [re.compile(pf(n), re.IGNORECASE) for n in names]

def memo(f):
    arr = []
    def helper():
        nonlocal arr
        if not arr:
            arr = f()
        return arr 
    return helper

@memo
def city_names():
    gc = geonamescache.GeonamesCache()
    cities = gc.get_cities()
    return [unidecode(cities[c]['name']) for c in cities]

@memo
def country_names():
    gc = geonamescache.GeonamesCache()
    countries = gc.get_countries()
    return [unidecode(countries[c]['name']) for c in countries]

@memo
def cities_re():
    return gen_re_arr(city_names(), name_pat_fun)

@memo
def countries_re():
    return gen_re_arr(country_names(), name_pat_fun)

def longest_match(matches):
    matches = list(set(matches))    # steps on duplicates
    if not matches:
        return None
    if len(matches) == 1:
        return matches[0]
    matches.sort(reverse=True, key=lambda s: len(s))
    return matches[0]

def find_match(re_arr, s):
    matches = []
    for r in re_arr:
        m = r.search(s)
        if m:
            matches.append(m[0])
    return longest_match(matches)

def main():
    from pandas import DataFrame
    headlines = [unidecode(h) for h in open("headlines.txt").readlines()]
    cities = [] 
    countries = [] 
    for h in headlines:
        cities.append(find_match(cities_re(), h))
        countries.append(find_match(countries_re(), h))
    df = DataFrame({'headline': headlines,
                    'countries': countries,
                    'cities': cities})

if __name__ == "__main__":
    main()

