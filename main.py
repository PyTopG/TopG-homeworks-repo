from src.widget import mask_account_card

test_data = (
    "Maestro 1596837868705199",
    "Счет 73654108430135874305",
    "Visa Classic 6831982476737658",
    "Счет 35383033474447895560",
)
for test_one in test_data:
    print(mask_account_card(test_one))
