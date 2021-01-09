from typing import List

try:
    from typing import TypedDict
except ImportError:
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
