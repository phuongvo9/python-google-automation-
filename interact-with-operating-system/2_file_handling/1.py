#!/usr/env/bin python3
import os
os.remove("spider.txt")
os.rename("first_draft.txt","finished_masterpiece.txt")
os.path.exists("finished_masterpeice.txt")