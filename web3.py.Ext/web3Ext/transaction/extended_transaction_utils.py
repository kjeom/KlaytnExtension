from typing import (
    Any,
    Dict,
    Sequence,
)
from toolz import (
    assoc,
    dissoc,
)
from transaction.extended_validation import (
    is_rpc_structured_signatures,
    is_rlp_structured_signatures,
)


# JSON-RPC to rlp transaction structure
def transaction_rpc_to_rlp_structure(dictionary: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert a JSON-RPC-structured transaction to an rlp-structured transaction.
    """
    signatures = dictionary.get("signatures")
    if signatures:
        dictionary = dissoc(dictionary, "signatures")
        rlp_structured_signatures = _signatures_rpc_to_rlp_structure(signatures)
        dictionary = assoc(dictionary, "signatures", rlp_structured_signatures)
    return dictionary


def _signatures_rpc_to_rlp_structure(signatures: Sequence) -> Sequence:
    if not is_rpc_structured_signatures(signatures):
        raise ValueError(
            "provided object not formatted as JSON-RPC-structured signatures"
        )
    rlp_structured_signatures = []
    for d in signatures:
        # flatten each dict into a tuple of its values
        rlp_structured_signatures.append(
            (
                d["v"], 
                d["r"], 
                d["s"], 
            )
        )
    return tuple(rlp_structured_signatures)


# rlp to JSON-RPC transaction structure
def transaction_rlp_to_rpc_structure(dictionary: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert an rlp-structured transaction to a JSON-RPC-structured transaction.
    """
    sitnatures = dictionary.get("signatures")
    if sitnatures:
        dictionary = dissoc(dictionary, "signatures")
        rpc_structured_signatures = _signatures_rlp_to_rpc_structure(sitnatures)
        dictionary = assoc(dictionary, "signatures", rpc_structured_signatures)
    return dictionary


def _signatures_rlp_to_rpc_structure(signatures: Sequence) -> Sequence:
    if not is_rlp_structured_signatures(signatures):
        raise ValueError("provided object not formatted as rlp-structured signatures")
    rpc_structured_signatures = []
    for t in signatures:
        # build a dictionary with appropriate keys for each tuple
        rpc_structured_signatures.append({"v": t[0], "r": t[1], "s": t[2]})
    return tuple(rpc_structured_signatures)