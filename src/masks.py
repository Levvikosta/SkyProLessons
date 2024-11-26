def get_mask_card_number(card_number: str) -> str:
    return str(card_number[0:7]) + "** ****" + str(card_number[-4:])


def get_mask_account(account: str) -> str:
    return "**" + str(account[-4:])
