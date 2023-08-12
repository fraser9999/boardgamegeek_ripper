readme.txt

Name:     Board Game Geek - Game Info Downloader/Ripper

Author:   Hermann Knopp

Contact:  hermann.knopp@gmx.at

Version:  0.1alpha (early alpha version)

Usage:    Python 3.10.10 Script for Ripping/Downloading
          Special Parts of the Game Board Geek
          Boardgame Database.

          (special use of custom traing a gpt2 chatbot model)

          Start: python bgg-ripper.py and wait for data
          
          a custom folder is generated where game text files
          are saved.      


Requirements: Install Python 3.10.10 x32 or x64/amd64

              Install "py-bgg" Library from github url
              (look at: readme-requirements.txt)

Files:    "bgg-ripper.py"

          Script for ripping BGG Data as Unformatted Text
          code will crash if garbage and special characters
          are in game data, please restart and resume

          "bgg-ripper2.py"

          Script for ripping BGG Data as Formatted Text
          code will crash if garbage and special characters
          are in game data, please restart and resume

          "bgg-ripper3.py"

          Script for ripping BGG Data,
          slightly improved Version, more Error tolerant,
          and new Status Messages as well as reformatted 
          Text Output, i believe it will not crash on
          special characters...


