from typing import Any


def validate_null_in_number_field(value: Any) -> Any:
    if not value:
        return 0
    return value
