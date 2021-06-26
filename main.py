from pyrogram import Client
import requests


@Client.on_message(
    filters.command(["start"], /)
