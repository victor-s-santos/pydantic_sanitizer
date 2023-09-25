from csv import DictReader
from typing import Any
from pydantic import BaseModel, conint, confloat, field_validator, FieldValidationInfo
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


def validate_null_in_number_field(value: Any) -> Any:
    if not value:
        return 0
    return value


class DadoCSV(BaseModel):
    """Realize the validation of each specific data format"""

    Company: str
    Item: str
    Calories: conint(ge=0) | None
    CaloriesFromFat: conint(ge=0) | None
    TotalFat: confloat(ge=0) | conint(ge=0) | None
    SaturatedFat: confloat(ge=0) | conint(ge=0) | None
    TransFat: confloat(ge=0) | conint(ge=0) | None
    Cholesterol: conint(ge=0) | None
    Sodium: conint(ge=0) | None
    Carbs: confloat(ge=0) | conint(ge=0) | None
    Fiber: confloat(ge=0) | conint(ge=0) | None
    Sugars: confloat(ge=0) | conint(ge=0) | None
    Protein: confloat(ge=0) | conint(ge=0) | None
    WeightWatchersPnts: confloat(ge=0) | str | None

    @field_validator("Calories")
    @classmethod
    def validate_calories(
        cls, value: int | None, info: FieldValidationInfo
    ) -> int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("CaloriesFromFat")
    @classmethod
    def validate_caloriesfromfat(
        cls, value: int | None, info: FieldValidationInfo
    ) -> int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("TotalFat")
    @classmethod
    def validate_totalfat(
        cls, value: float | int | None, info: FieldValidationInfo
    ) -> float | int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("SaturatedFat")
    @classmethod
    def validate_saturedfat(
        cls, value: float | int | None, info: FieldValidationInfo
    ) -> float | int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("TransFat")
    @classmethod
    def validate_transfat(
        cls, value: float | int | None, info: FieldValidationInfo
    ) -> float | int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("Cholesterol")
    @classmethod
    def validate_cholesterol(
        cls, value: int | None, info: FieldValidationInfo
    ) -> int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("Sodium")
    @classmethod
    def validate_sodium(
        cls, value: int | None, info: FieldValidationInfo
    ) -> int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("Carbs")
    @classmethod
    def validate_carbs(
        cls, value: float | int | None, info: FieldValidationInfo
    ) -> float | int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("Fiber")
    @classmethod
    def validate_fiber(
        cls, value: float | int | None, info: FieldValidationInfo
    ) -> float | int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("Sugars")
    @classmethod
    def validate_sugars(
        cls, value: float | int | None, info: FieldValidationInfo
    ) -> float | int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("Protein")
    @classmethod
    def validate_protein(
        cls, value: float | int | None, info: FieldValidationInfo
    ) -> float | int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("WeightWatchersPnts")
    @classmethod
    def validate_weightwatcherspnts(
        cls, value: float | int | None, info: FieldValidationInfo
    ) -> float | int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)


if __name__ == "__main__":
    fast_food_values = transform_csv_to_dictionary("FastFoodNutritionMenu")
