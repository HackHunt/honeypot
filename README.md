## Honeypot

- A honeypot is a computer security mechanism set to detect, deflect, or, in some manner, counteract 
attempts at unauthorized use of information systems. 
- It attracts Cyber Attacks by mimicking as a target for the attacker. 
- Also, used as a distraction for hackers from the real target. 
- The Program generates a log file containing attacker's IP, Port and Time of
when conncetion was made.

### Supports Platform:
Linux, Debain

### How to use:
- Convert the setup.sh into executable
	> **chmod 755 setup.sh**
- Run setup.sh
	> **./setup.sh**
- Run the Python Script with root privileges.
    > **sudo python3 honeypot.py** 


### Available Arguments:
- **-h or --help:** *Displays all the available options.*
- **-ip or --host-ip**: *Specify the IPv4 Address of the Host.*
- **-d or --tarp-data:** *If someone tries to connect to the port specified this data will be sent.*
- **-p or --port:** *Specify port number to create Honeypot on.*


### Color:

- **Green:** Successful.
- **Yellow:** Notifications.
- **Blue:** Activities.
- **Red:** Unsuccessful or Errors. 

### Programming Language: Python 3 and above

### Licensed: GNU General Public License, version 3

### Developer Information:
- **Website:** https://www.hackhunt.in/
- **Contact:** hh.hackunt@gmail.com
- **LinkedIn:** https://www.linkedin.com/company/hackhunt
- **Youtube:** [@hackhunt](https://youtube.com/hackhunt)
- **Instagram:** [@hh.hackhunt](https://www.instagram.com/hh.hackhunt/)
- **Facebook:** [@hh.hackhunt](https://www.facebook.com/hh.hackhunt/)
- **Twitter:** [hh_hackhunt](https://twitter.com/hh_hackhunt/)
- **Patreon:** [@hackhunt](https://www.patreon.com/hackhunt)
