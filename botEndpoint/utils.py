from discord.ext import commands, tasks
from dataclasses import dataclass
import datetime
import discord
from discord import app_commands
from config import Config
from config import bot
from datetime import datetime, timedelta
from loguru import logger
from db import get_session
from model import User_info, Emoji_info
import numpy as np
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/calendar']
service = None

async def calendar_setting():

    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
    except HttpError as error:
        print('An error occurred: %s' % error)
    
    return service

async def get_points_message(points : int, query : bool):

    session = get_session()

    emoji_number = ""
    for char in str(points):
        emoji = session.query(Emoji_info).filter(Emoji_info.emoji_name == int(char)).first()
        emoji_number += f"<:{emoji.emoji_eng}:{emoji.emoji_id}>"

    if query: 
        return f"您的 G token 目前已累積 {points} :coin:\n{emoji_number}"

    else:
        return f"您醬獲得了 {points} :coin:\n{emoji_number}"