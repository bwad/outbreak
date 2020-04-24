
from . headlines import (
    longest_match,
    cities_re,
    countries_re,
    find_match,
    city_names
)

def test_canary():
    assert 1 == 1 

def test_longest_match():
    matches = ["one", "onetwo"]
    assert longest_match(matches) == "onetwo"

def test_hit():
    h = 'Kuala Lumpur is Hit By Zika Threat\n' 
    cities = cities_re()
    matches = []
    for c in cities:
        m = c.search(h)
        if m:
            matches.append(m[0])
    assert matches == ['Hit', 'Kuala Lumpur']

CITIES = city_names()

def test_hit_city():
    # Headline 'Kuala Lumpur is Hit By Zika Threat\n' produces the
    # following match ['Kuala Lumpur', 'Hit'] because 'Hit' is a city. 
    assert 'Hit' in CITIES 

def test_ho_city():
    # Heading "Zika cases in Vietnam's Ho Chi Minh City surge\n" 
    # produces the followin match ['Ho Chi Minh City', 'Ho'] because
    # 'Ho' is a city. 
    assert 'Ho' in CITIES 

def test_no_loilo_city():
   # (None, 'Iloilo', 'Zika afflicts 7 in Iloilo City\n')
   ic = "Iloilo City"
   assert ic not in CITIES

def test_no_tampa_bay_city():
    # (None, 'Tampa', 'Tampa Bay Area Zika Case Count Climbs\n')
    tb = 'Tampa Bay'
    assert tb not in CITIES

def test_not_sarasota_county():
    # (None, 'Sarasota', 'New Zika Case Confirmed in Sarasota County\n')
    assert 'Sarasota County' not in CITIES

def test_not_Hillsborough():
    # (None, None, 'Hillsborough uses innovative trap against Zika 20 minutes ago\n')
    assert 'Hillsborough' not in CITIES

def test_not_Oton():
    # (None, None, 'Zika case reported in Oton\n'
    assert 'Oton' not in CITIES

def test_not_Antigua():
    # (None, None, 'Spanish Flu Sighted in Antigua\n')
    assert 'Antigua' not in CITIES

def test_not_rio_de_janeiro():
    # (None, None, 'Carnival under threat in Rio De Janeiro due to Zika outbreak\n'
    assert 'Rio De Janeiro' not in CITIES

# ('Thailand', 'Bangkok', 'Thailand-Zika Virus in Bangkok\n')
# ('Guatemala', 'Guatemala City', 'Rumors about Meningitis spreading in Guatemala City have been refuted\n')
# ('Belize', 'Belize City', 'Belize City under threat from Zika\n')
# (None, 'Quebec', 'Hepatitis B Vaccine is now Required in Quebec\n')
# ('Mexico', 'Mexico City', 'Zika outbreak spreads to Mexico City\n')
# (None, None, 'Maka City Experiences Influenza Outbreak\n')
# (None, 'Belo Horizonte', 'New Zika Case Confirmed in Belo Horizonte\n')