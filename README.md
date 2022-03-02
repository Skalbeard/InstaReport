instagram reporter

* download and install Docker from here https://docs.docker.com/desktop/windows/install/
* you also might need to install WSL2 patch afterwards. it will tell you if you need to, just follow the link and download and install that too.
* restart your computer
* clone or download the project from here https://github.com/Skalbeard/InstaReport
* open CMD or PowerShell in that project folder (same way as with telrep)
* run command		docker pull skalbe/ohlol:latest
* run command		docker build -t skalbe/ohlol .    (the space and the dot INCLUDED)
* run command		docker run skalbe/ohlol
IF the command above gives you an error
	* run command		 docker run -it skalbe/ohlol bash
	* now you are in root access. run command			 ./entry-point.sh
