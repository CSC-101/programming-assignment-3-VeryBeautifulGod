from data import CountyDemographics
#Part 1
def population_total(county_list: list[CountyDemographics]) -> int:
    total_population = 0
    for county in county_list:
        total_population += county.population.get('2014', 0)
    return total_population

#Part 2
def filter_by_state(county_list: list[CountyDemographics], state_abbr: str) -> list[CountyDemographics]:
    result = []
    for county in county_list:
        if county.state == state_abbr:
            result.append(county)
    return result
#Part 3
def population_by_education(county_list: list[CountyDemographics], education_key: str) -> float:
    total_population = 0
    for county in county_list:
        population_2014 = county.population.get('2014', 0)
        education_percentage = county.education.get(education_key, 0)
        total_population += population_2014 * (education_percentage / 100)
    return total_population

def population_by_ethnicity(county_list: list[CountyDemographics], ethnicity_key: str) -> float:
    total_population = 0
    for county in county_list:
        population_2014 = county.population.get('2014', 0)
        ethnicity_percentage = county.ethnicities.get(ethnicity_key, 0)
        total_population += population_2014 * (ethnicity_percentage / 100)
    return total_population

def population_below_poverty_level(county_list: list[CountyDemographics]) -> float:
    total_population = 0
    for county in county_list:
        population_2014 = county.population.get('2014', 0)
        poverty_percentage = county.income.get('Persons Below Poverty Level', 0)
        total_population += population_2014 * (poverty_percentage / 100)
    return total_population
#Part 4
def percent_by_education(county_list: list[CountyDemographics], education_key: str) -> float:
    total_population = 0
    total_education_population = 0
    for county in county_list:
        population_2014 = county.population.get('2014', 0)
        education_percentage = county.education.get(education_key, 0)
        total_population += population_2014
        total_education_population += population_2014 * (education_percentage / 100)

    if total_population == 0:
        return 0
    return (total_education_population / total_population) * 100

def percent_by_ethnicity(county_list: list[CountyDemographics], ethnicity_key: str) -> float:
    total_population = 0
    total_ethnicity_population = 0
    for county in county_list:
        population_2014 = county.population.get('2014', 0)
        ethnicity_percentage = county.ethnicities.get(ethnicity_key, 0)
        total_population += population_2014
        total_ethnicity_population += population_2014 * (ethnicity_percentage / 100)

    if total_population == 0:
        return 0
    return (total_ethnicity_population / total_population) * 100

def percent_below_poverty_level(county_list: list[CountyDemographics]) -> float:
    total_population = 0
    total_poverty_population = 0
    for county in county_list:
        population_2014 = county.population.get('2014', 0)
        poverty_percentage = county.income.get('Persons Below Poverty Level', 0)
        total_population += population_2014
        total_poverty_population += population_2014 * (poverty_percentage / 100)

    if total_population == 0:
        return 0
    return (total_poverty_population / total_population) * 100

#Part 5
def education_greater_than(county_list: list[CountyDemographics], education_key: str, threshold: float) -> list[CountyDemographics]:
    result = []
    for county in county_list:
        education_percentage = county.education.get(education_key, 0)
        if education_percentage > threshold:
            result.append(county)
    return result

def education_less_than(county_list: list[CountyDemographics], education_key: str, threshold: float) -> list[CountyDemographics]:
    result = []
    for county in county_list:
        education_percentage = county.education.get(education_key, 0)
        if education_percentage < threshold:
            result.append(county)
    return result

def ethnicity_greater_than(county_list: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
    result = []
    for county in county_list:
        ethnicity_percentage = county.ethnicities.get(ethnicity_key, 0)
        if ethnicity_percentage > threshold:
            result.append(county)
    return result

def ethnicity_less_than(county_list: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
    result = []
    for county in county_list:
        ethnicity_percentage = county.ethnicities.get(ethnicity_key, 0)
        if ethnicity_percentage < threshold:
            result.append(county)
    return result

def below_poverty_level_greater_than(county_list: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    result = []
    for county in county_list:
        poverty_percentage = county.income.get('Persons Below Poverty Level', 0)
        if poverty_percentage > threshold:
            result.append(county)
    return result

def below_poverty_level_less_than(county_list: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    result = []
    for county in county_list:
        poverty_percentage = county.income.get('Persons Below Poverty Level', 0)
        if poverty_percentage < threshold:
            result.append(county)
    return result
