#!env/python3
from app import custom_time 
from app import sort
import sys

if __name__ == "__main__": 
    # if sys.argv[1] == "now":
    #     sort.start_sorting()
    timee = sys.argv[1]
    # i'll complete it later
    
    custom_time.check_time(timee)