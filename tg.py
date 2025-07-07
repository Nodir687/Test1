import asyncio
from aiogram import Bot, Dispatcher, Router, F, types
from aiogram.types import KeyboardButton, InlineKeyboardButton, Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

bot = Bot(token="8090500863:AAEBTD3Cqm0URRynfVskKaZYiQs_-1C6530")
dp = Dispatcher()
router = Router()

class statuslar(StatesGroup):
    name = State()
    phone = State()
    age = State()

def telefon_keyboard():
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(
        KeyboardButton(text="Telefon raqamni yuboring!", request_contact=True),
                KeyboardButton(text="Orqaga"),
        )
    keyboard.adjust(1)
    return  keyboard.as_markup(resize_keyboard=True, input_field_placeholder='Telefon raqamni kiriting')

@router.message(F.text.startswith("/start"))
async def start_menu(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await message.answer("Assalomu Aleykum bizning botga xush kelibsiz.\n<b>Iltimos, ismingizni kiriting</b>", parse_mode='HTML')

@router.message(statuslar.age)
async def age_menu(message: Message, state: FSMContext):
    user_id = message.from_user.id
    data = await state.get_data()
    msg_text = (
        f"Ismingiz - {data['name']}\n"
        f"Telefon raqamingiz - {data['phone']}\n"
        f"Yoshingiz - {message.text}"
    )
    if message.text == "Orqaga":
        await message.answer("Telefon raqamingizni kiriting", reply_markup=telefon_keyboard())
        await state.set_state(statuslar.phone)
    elif message.text.isdigit():
        await state.update_data(age=message.text)
        await message.answer("Yoshingiz kiritildi.\nZayavka yaratildi")
        await message.answer(msg_text)
        await state.clear()
    else:
        await message.answer("Iltimos raqamda kiriting")

    await state.set_state(statuslar.name)


@router.message(statuslar.name)
async def name_menu(message: Message, state: FSMContext):
    user_id = message.from_user.id
    await state.update_data(name=message.text)
    await message.answer(text="Telefon raqamni kirgizish", reply_markup=telefon_keyboard())
    await state.set_state(statuslar.phone)


@router.message(statuslar.phone)
async def phone_menu(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if message.text == "Orqaga":
        await message.answer("Ismingiz kiriting", reply_markup=ReplyKeyboardRemove())
        await state.set_state(statuslar.name)
    elif message.contact:
        await state.update_data(phone=message.contact.phone_number)
        await message.answer("Yoshingizni kiriting", reply_markup=back())
        await state.set_state(statuslar.age)
    else:
        text = message.text
        if message.text.startswith("+998") and len(text) == 13 and text[1:].isdigit():
            await state.update_data(phone=message.text)
            await message.answer("Yoshingizni kiriting", reply_markup=back())
            await state.set_state(statuslar.age)
        else:
            await message.answer("Iltimos telefon raqamingiz togri formatda kiriting")

def back():
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(KeyboardButton(text="Orqaga"))
    return keyboard.as_markup(resize_keyboard=True, input_field_placehodler="Yoshingizni kiriting")
