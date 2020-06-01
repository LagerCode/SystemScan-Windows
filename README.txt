This is a gui application which is meant for checking hardware info, Os info, network info and actions such as checking the connection speed with speedtest and running a antivirus scan.

The program is a python application where tkinter is responsible for the gui and powershell for the button functions. 
The program works but it crashes if you click while it's running windows defender or checking the connection, seems to be tkinter since it doesn't crash while running as cli.

Things to improve: change GUI tech to Qt or similar
		   remove the curly brackets and the string "None" from the display window