# library/fine.py

def calculate_fine(days_late):
    """
    Week 1 (days 1-7 late): 10 Rs per day per book
    Week 2 (days 8-14 late): 20 Rs per day per book
    Week 3 (days 15-21 late): 60 Rs per day per book
    Week 4 and beyond (days 22+ late): 120 Rs per day per book
    """
    if days_late <= 0:
        return 0
        
    fine = 0
    if days_late <= 7:
        fine = days_late * 10
    elif days_late <= 14:
        # Week 1 full fine + remaining days of Week 2
        fine = (7 * 10) + ((days_late - 7) * 20)
    elif days_late <= 21:
        # Week 1 + Week 2 full fine + remaining days of Week 3
        fine = (7 * 10) + (7 * 20) + ((days_late - 14) * 60)
    else:
        # Week 1 + Week 2 + Week 3 full fine + remaining days of Week 4+
        fine = (7 * 10) + (7 * 20) + (7 * 60) + ((days_late - 21) * 120)
        
    return fine
