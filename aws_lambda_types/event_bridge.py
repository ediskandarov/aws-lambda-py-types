from typing import List

from typing_extensions import TypedDict

ScheduledEventDict = TypedDict(
    "ScheduledEventDict",
    {
        "account": str,
        "detail-type": str,
        "detail": dict,
        "id": str,
        "region": str,
        "resources": List[str],
        "source": str,
        "time": str,
    },
)
