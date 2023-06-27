def make_readable(seconds):
    # # Do something
    sec = 0
    minute = 0
    hour = 0

    while True:
        remain = seconds // 3600
        remain1 = seconds // 60
        
        if remain > 0:
            hour += remain
            seconds = seconds - (remain*3600)
        
        else:
            if remain1 > 0:
                minute += remain1
                seconds = seconds - (remain1*60)
                
            elif remain1 <= 0:
                sec = seconds
                break
            
    return "{:02d}:{:02d}:{:02d}".format(hour, minute, sec)



if __name__ == '__main__':
    seconds = 86399
    print(make_readable(seconds))
    seconds = 359999
    print(make_readable(seconds))
    seconds = 3600
    print(make_readable(seconds))