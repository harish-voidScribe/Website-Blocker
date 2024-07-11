import time
from datetime import datetime as dt, timedelta


blocked_websites = ["www.facbook.com"]
#ADD RQUIRED WEBSITES INTO THE LIST 
start_hour = 9  
start_minute = 0  
end_hour = 17  
end_minute = 0  

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

redirect_ip = "127.0.0.1"

def get_block_times():
    now = dt.now()
    start_time = dt(now.year, now.month, now.day, start_hour, start_minute)
    end_time = dt(now.year, now.month, now.day, end_hour, end_minute)
    if end_time <= start_time:
        end_time += timedelta(days=1) 
    return start_time, end_time

def block_websites():
    while True:
        start_time, end_time = get_block_times()
        current_time = dt.now()
        if start_time <= current_time <= end_time:
            try:
                with open(hosts_path, "r+") as file:
                    content = file.read()
                    for website in blocked_websites:
                        entry = f"{redirect_ip} {website}\n"
                        if entry not in content:
                            file.write(entry)
            except PermissionError:
                print("Permission denied: Please run the script as an administrator.")
                break
        else:
            try:
                with open(hosts_path, "r+") as file:
                    content = file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any(website in line for website in blocked_websites):
                            file.write(line)
                    file.truncate()
            except PermissionError:
                print("Permission denied: Please run the script as an administrator.")
                break
        time.sleep(60) 

if __name__ == "__main__":
    block_websites()


#to unblock the website go to C:\Windows\System32\drivers\etc\ and toggle from text documents to All files 
#Then click on the hosts file 
#remove 127.0.0.1:www.youtube.com