from csv import DictReader, DictWriter
from models.data_models import DadoCSV
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


def write_csv_from_valid_data(
    list_trust_data: list, output_filename: str = "output_files/cleaned_data.csv"
) -> str:
    """Export the csv from given valid data

    Args:
        list_trust_data (list): The list of trust_data

    Returns:
        str: The success message
    """

    colunm_names = [
        "Company",
        "Item",
        "Calories",
        "CaloriesFromFat",
        "TotalFat",
        "SaturatedFat",
        "TransFat",
        "Cholesterol",
        "Sodium",
        "Carbs",
        "Fiber",
        "Sugars",
        "Protein",
        "WeightWatchersPnts",
    ]
    with open(output_filename, "w") as file:
        csv_file = DictWriter(file, fieldnames=colunm_names)

        for data in list_trust_data:
            csv_file.writerow(dict(data))

    return f"The file has been exported in {output_filename} destination."


if __name__ == "__main__":
    fast_food_values = transform_csv_to_dictionary("FastFoodNutritionMenu")

    list_trust_data = []
    list_trash_data = []

    for value in fast_food_values:
        try:
            cleaned_data = DadoCSV(**value)
            list_trust_data.append(cleaned_data.model_dump())

        except Exception:
            list_trash_data.append({"Valor com problema": value})
