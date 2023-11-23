from typing import Any, Callable, Coroutine, cast
from telethon import events # pyright: ignore


def query_data_starts_with(starts_with: str) -> Callable[[events.CallbackQuery.Event], Coroutine[Any, Any, bool]]:
    async def inner(e: events.CallbackQuery.Event) -> bool:
        return str(e.query.data.decode()).startswith(starts_with)   # pyright: ignore

    return inner


def chat_message(chats_id: int) -> Callable[[events.NewMessage.Event], Coroutine[Any, Any, bool]]:
    async def inner(e: events.NewMessage.Event) -> bool:
        chat_id = cast(int, e.chat_id)  # pyright: ignore
        return chat_id == chats_id

    return inner

def message_from_chatslist(chat_ids: list[int]) -> Callable[[events.NewMessage.Event], Coroutine[Any, Any, bool]]:
    async def inner(e: events.NewMessage.Event) -> bool:
        chat_id = cast(int, e.chat_id)  # pyright: ignore
        return chat_id in chat_ids

    return inner