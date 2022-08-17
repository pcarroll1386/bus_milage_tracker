all_busses = [
    {
        "buss_number": "1",
        "last_logged_miles": 34825
    },
    {
        "buss_number": "2",
        "last_logged_miles": 34825
    },
    {
        "buss_number": "3",
        "last_logged_miles": 34825
    },
    {
        "buss_number": "4",
        "last_logged_miles": 34825
    },
    {
        "buss_number": "5",
        "last_logged_miles": 34825
    },
    {
        "buss_number": "6",
        "last_logged_miles": 34825
    }
]

def get_all():
    return all_busses

def get_by_id(buss_id):
    for buss in all_busses:
        if buss_id == buss.buss_number:
            return buss
    return None

def add(buss):
    for stored_buss in all_busses:
        if stored_buss.buss_number == buss.buss_number:
            return None
    all_busses.append(buss)
    return buss

def update(buss):
    for updated_buss in all_busses:
        if buss.busss_id == updated_buss.buss_number:
            updated_buss.last_logged_miles = buss.last_logged_miles

def delete(buss_id):
    if all_busses["buss_id"] == buss_id:
        del all_busses[buss_id]