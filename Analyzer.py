file=open("log.txt", "r")
data={}
threshold=3
for line in file:
    char_line=line.strip()
    if char_line=="":
        continue
    parts=char_line.split("-")
    ip=parts[0].strip()
    status=parts[1].strip()
    if ip not in data:
        data[ip]={
            "failed":0,
            "success":0
		}
    if status=="FAILED":
        data[ip]["failed"]+=1
    else:
        data[ip]["success"]+=1
print("\n--- Log Analysis Report ---\n")

for ip, counts in data.items():
    status_flag = ""
    
    if counts["failed"] > threshold:
        status_flag = " 🚨 Suspicious"
    
    print(f"IP: {ip} | Failed: {counts['failed']} | Success: {counts['success']}{status_flag}")
file.close()