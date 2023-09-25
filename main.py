from csv import DictReader
from pydantic import BaseModel, conint
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
    Calories: conint(gt=0)
    CaloriesFromFat: conint(gt=0)
    TotalFat: float | conint(gt=0)
    SaturatedFat: float | conint(gt=0)
    TransFat: float | conint(gt=0)
    Cholesterol: conint(gt=0)
    Sodium: conint(gt=0)
    Carbs: float | conint(gt=0)
    Fiber: float | conint(gt=0)
    Sugars: float | conint(gt=0)
    Protein: float | conint(gt=0)
    WeightWatchersPnts: float | str | None


if __name__ == "__main__":
    fast_food_values = transform_csv_to_dictionary("FastFoodNutritionMenu")
