"""A tool to filter an ApplicationSnapshot based on a mapping"""

import json
import sys


class FilteredComponent(dict):
    """A class to hold component data after it is filtered"""

    component: str
    srcImageURL: str
    destImageUrl: str


def filter_snapshot(snapshot: dict, mapping: dict) -> list:
    """Filter an ApplicationSnapshot given a mapping

    The returned list will contain only the components that
    are present in the mapping. Each entry will contain the
    component name, its source URL and its destination URL
    from the mapping.

    :param snapshot: ApplicationSnapshot to filter
    :param mapping: mapping to apply to the snapshot
    :returns: filtered list of components"""

    filtered_snapshot = []
    for img in mapping:
        for component in snapshot["images"]:
            if img["component"] == component["component"]:
                filtered_snapshot.append(
                    FilteredComponent(
                        component=img["component"],
                        srcImageURL=component["pullSpec"],
                        destImageURL=img["destination"],
                    )
                )
    return filtered_snapshot


def main() -> None:
    """Create a filtered snapshot given cli args"""

    snapshot = json.loads(sys.argv[1])
    mapping = json.loads(sys.argv[2])

    print(filter_snapshot(snapshot, mapping))


if __name__ == "__main__":
    main()
