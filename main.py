from csv import DictReader
from pydantic import BaseModel, FieldValidationInfo, field_validator
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
    # TODO fix the keys name
    # TotalFat_g: float
    # SaturatedFat_g: float
    # TransFat_g: float
    # Cholesterol_mg: int
    # Sodium_mg: int
    # Carbs_g: float
    # Fiber_g: float
    # Sugars_g: float
    # Protein_g: float
    WeightWatchersPnts: float

    @field_validator("Company")
    @classmethod
    def validate_company(cls, value: str, info: FieldValidationInfo) -> str:
        logging.info(info.config.get("title"))
        return value

    @field_validator("Item")
    @classmethod
    def validate_item(cls, value: str, info: FieldValidationInfo) -> str:
        logging.info(info.config.get("title"))
        return value

    @field_validator("Calories")
    @classmethod
    def validate_calories(cls, value: int, info: FieldValidationInfo) -> int:
        logging.info(info.config.get("title"))
        return value

    @field_validator("CaloriesFromFat")
    @classmethod
    def validate_caloriesfromfat(cls, value: int, info: FieldValidationInfo) -> int:
        logging.info(info.config.get("title"))
        return value

    @field_validator("WeightWatchersPnts")
    @classmethod
    def validate_weightwatcherspnts(
        cls, value: float, info: FieldValidationInfo
    ) -> float:
        logging.info(info.config.get("title"))
        return value


if __name__ == "__main__":
    fast_food_values = transform_csv_to_dictionary("FastFoodNutritionMenu")
