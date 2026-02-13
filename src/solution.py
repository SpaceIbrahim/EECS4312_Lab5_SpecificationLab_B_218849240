## Student Name: Muhammad Ibrahim
## Student ID: 218849240

"""
Stub file for the is allocation feasible exercise.

Implement the function `is_allocation_feasible` to  Determine whether a set of resource requests can be satisfied 
given limited capacities. Take int account any possible constraints. See the lab handout
for full requirements.
"""
    
from typing import Dict, List, Union

Number = Union[int, float]


def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    """
    Determine whether a set of resource requests can be satisfied given limited capacities.

    Args:
        resources : Dict[str, Number], Mapping from resource name to total available capacity.
        requests : List[Dict[str, Number]], List of requests. Each request is a mapping from resource name to the amount required.

    Returns:
        True if the allocation is feasible, False otherwise.

    """
    # TODO: Implement this function
    available = resources.copy()
    for request in requests:
        if not isinstance(request, dict):
            raise ValueError("Each request must be a dictionary.")
        for resource, amount in request.items():
            if resource not in available:
                return False
            available[resource] -= amount
            if available[resource] < 0:
                return False
    
    # Addition of new requirement: Check for at least one resource remaining with at least one after assignment.
    # If all resources have zero or negative capacity, the allocation is not feasible.
    # Because it does not meet the new requirement:
    # "At least one resource must remain unallocated after assignment."
    # AND
    # "An allocation that satisfies all requests but consumes all available resource is no longer valid."
    # Using these addition requirements given to us, we take that asking for having any resource be left
    # with at least one unit of resource after allocation.
    # This is the best guess we can make given the vague wording of the new requirement.
    if not any(amount > 0 for amount in available.values()):
        return False
    return True