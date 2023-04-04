from cytoolz import (
    identity,
)
from eth_utils import (
    is_binary_address,
    is_checksum_address,
    is_dict,
)
from eth_utils.curried import (
    apply_one_of_formatters,
    hexstr_if_str,
    is_0x_prefixed,
    is_address,
    is_bytes,
    is_integer,
    is_list_like,
    is_string,
    to_bytes,
    to_int,
)

def is_int_or_prefixed_hexstr(val):
    if is_integer(val):
        return True
    elif isinstance(val, str) and is_0x_prefixed(val):
        return True
    else:
        return False

def is_rpc_structured_signatures(val):
    """Returns true if 'val' is a valid JSON-RPC structured signatures."""
    if not is_list_like(val):
        return False
    for d in val:
        if not is_dict(d):
            return False
        if len(d) != 3:
            return False
        v = d.get('v')        
        r = d.get('r')
        s = d.get('s')
        if any(_ is None for _ in (v,r,s)):
            return False
        # if not is_int_or_prefixed_hexstr(v):
        #     return False
        # if not is_int_or_prefixed_hexstr(r):
        #     return False
        # if not is_int_or_prefixed_hexstr(s):
        #     return False
    return True


def is_rlp_structured_signatures(val):
    """Returns true if 'val' is a valid rlp-structured signatures."""
    if not is_list_like(val):
        return False
    for item in val:
        if not is_list_like(item):
            return False
        if len(item) != 3:
            return False
        v, r, s = item
        # if not is_int_or_prefixed_hexstr(v):
        #     return False
        # if not is_int_or_prefixed_hexstr(r):
        #     return False
        # if not is_int_or_prefixed_hexstr(s):
        #     return False
    return True