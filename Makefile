#!/bin/bash
# Makefile for CSCI 315 - Lab 3
# 
all: main

main: Main.py Element.py Player.py
	pyinstaller --onefile Main.py
	cp ./dist/Main ./Main

.PHONY: all main