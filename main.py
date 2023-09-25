from csv import DictReader
from pydantic import BaseModel
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
    TotalFat: float | int
    SaturatedFat: float | int
    TransFat: float | int
    Cholesterol: int
    Sodium: int
    Carbs: float | int
    Fiber: float | int
    Sugars: float | int
    Protein: float | int
    WeightWatchersPnts: float | str | None


if __name__ == "__main__":
    fast_food_values = transform_csv_to_dictionary("FastFoodNutritionMenu")
