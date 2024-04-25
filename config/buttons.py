from telegram import InlineKeyboardButton, KeyboardButton


info_btns = [
    [
        InlineKeyboardButton("Edit Data", callback_data="edit_data"),
        InlineKeyboardButton("Main Menu", callback_data="main_menu"),
    ],

]

gender_btns = [
    [KeyboardButton("Male"), KeyboardButton("Female")]
]

info_edit_btns = [
    [
        KeyboardButton("Edit"),
        KeyboardButton("Save"),
    ]
]

main_btns = [
    [
        KeyboardButton("Main menu"),
        KeyboardButton("My info")
    ]
]

user_edit_btns = [
    [
        InlineKeyboardButton(
            "First Name", callback_data="edit_first_name"),
        InlineKeyboardButton(
            "Last Name", callback_data="edit_last_name"),
    ],
    [
        InlineKeyboardButton("Age", callback_data="edit_age"),
        InlineKeyboardButton(
            "Gender", callback_data="edit_gender"),
    ],
    [
        InlineKeyboardButton(
            "Contact", callback_data="edit_contact"),
        InlineKeyboardButton(
            "Address", callback_data="edit_address")
    ],
]

contact_btns = [
    [KeyboardButton("Share", request_contact=True)]
]
