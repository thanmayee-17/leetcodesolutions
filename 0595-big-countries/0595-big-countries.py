import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    bigCountries_filters=(world['area']>=3000000)|(world['population']>=25000000)
    return world.loc[bigCountries_filters,['name','population','area']]
    