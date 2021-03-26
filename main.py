from pyrogram import Client, filters
from pyrogram.raw import functions

app = Client("block-telegram-spam")


@app.on_message(filters.incoming & filters.private & filters.document)
def handle_message(client, message):
    if not message.from_user.is_contact:
        # log message
        print(message)
        # report spam
        client.send(
            functions.messages.ReportSpam(
                peer=client.resolve_peer(message.from_user.id),
            )
        )
        # block user
        client.block_user(message.from_user.id)
        # delete chat (commented out while the script is being tested)
        # client.send(
        #     functions.messages.DeleteChat(
        #         chat_id=message.chat.id
        #     )
        # )


app.run()
