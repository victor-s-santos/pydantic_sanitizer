from csv import DictReader
from pydantic import BaseModel, validator
import logging


def transform_csv_to_dictionary(file_name: str) -> list:
    """Apply DictReader method over a given csv file and returns a list of dictionaries of each value in the csv.

    Args:
        file_name (str): The csv file name in the input_files directory.

    Returns:
        list: Theee list of dictionaries for each key value in the given csv.
    """
    file_address = f"input_files/{file_name}.csv"
    try:
        with open(file_address, "r") as file:
            dict_objs = DictReader(file)
            list_of_values = [dicio for dicio in dict_objs]
        return list_of_values

    except Exception as e:
        logging.error(f"Can't get list from given csv file name: {e}")


class DadoCSV(BaseModel):
    """Realize the validation of each specific data format"""

    Company: str
    Item: str
    Calories: int
    CaloriesFromFat: int
    TotalFat_g: float
    SaturatedFat_g: float
    TransFat_g: float
    Cholesterol_mg: int
    Sodium_mg: int
    Carbs_g: float
    Fiber_g: float
    Sugars_g: float
    Protein_g: float
    WeightWatchersPnts: int

    @validator("TotalFat_g", pre=True)
    def validate_total_fat(cls, value):
        if "TotalFat(g)" in cls.__annotations__:
            """This if is necessary because has (g) in the name of the field"""
            return value
        raise ValueError("Field 'TotalFat(g)' is required.")


if __name__ == "__main__":
    fast_food_values = transform_csv_to_dictionary("FastFoodNutritionMenu")

# TODO
# Migrate to Pydantic V2 Style
