from typing import TypedDict, List


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
