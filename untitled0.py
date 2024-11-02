#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 19:02:29 2024

@author: ravi
"""
print("hello")
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()  # Load .env file
API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')