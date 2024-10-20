# Hearing Aids Fitting Software Update Checkers
![GitHub all releases](https://img.shields.io/github/downloads/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/total?style=for-the-badge)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers?label=LATEST%20RELEASE&style=for-the-badge)
<br/>
![GitHub commits since tagged version](https://img.shields.io/github/commits-since/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/latest?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers?style=for-the-badge)

A collection of scripts which check hearing aids fitting software directly from their company's servers.

## What does it do?
This repository contains scripts which can check hearing aids fitting software (such as Phonak Target) directly from the software's servers, avoiding the need to distribute copyrighted files. (I am not a lawyer, this is not legal advice, this is merely my opinion.)

## Currently supported software
The script currently supports:
- Sonova
  - Phonak Target
    - Phonak Target Media
    - Phonak Target Sounds
  - Unitron TrueFit
  - Hansaton scout
- Demant
  - Oticon Genie 2 (v2024+)
  - Oticon Genie
  - Bernafon OasisNXT (v2024+)
  - Sonic ExpressFit (v2024+)
  - Philips HearSuite (v2024+)
- GN
  - ReSound Smart Fit
  - Resound Aventa
  - ReSound Pro-Counsel
  - Beltone Solus Max
  - Beltone Solus
  - Beltone SelectaFit
  - Interton Fitting
  - Interton Appraise
  - Interton CompuFit
- WS Audiology
  - Signia Connexx
  - Rexton Connexx
  - Audio Service Connexx
  - A&M Connexx
  - Widex Compass GPS
- Starkey
  - Starkey Pro Fit
  - Starkey Inspire OS

## Where to get it
The script is available here: https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/releases/latest

Note: You need to have the latest version of Python installed for this to work.
## How to use it
1. Download the script from here: https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/releases/latest<br/>
   Click on the link and then click on the `Hearing-Aids-Fitting-Software-Update-Checkers.zip` link to download it
2. Extract the ZIP to a folder
3. Go to: https://www.python.org/downloads/
4. Click on the yellow `Download Python` button and run the installer
5. Make sure you select `Add python.exe to PATH` in the start of the installer, and then click on `Install Now`
6. **Reboot your computer**
7. Now go back to the folder where you extracted the scripts (not the ZIP file, the extracted folder)
8. Double-click the `start-Windows.bat` file and follow the instructions on-screen

NOTE: If the script looks like it has frozen, then try disabling `quickEdit` by running the `fixQuickedit.reg` file before running `start-Windows.bat`

## Credits
- [@Bluebotlabz](https://github.com/Bluebotlabz): Original author of this script
- [@pvc](https://forum.hearingtracker.com/u/tenkan): Assisting with testing of the script and finding software links
- [@tenkan](https://forum.hearingtracker.com/u/tenkan): Finding the Genie (2) download page links

## Changelog
### v2024.08.31
- Name changes
- Versoning scheme changes to date-based
- Add support for A&M Connexx
- Add support for Audio Services Connexx
- Add support for Bernafon OasisNXT v2024+
- Add support for Hansaton scout
- Add support for Oticon Genie 2 v2024+
- Add support for Philips HearSuite v2024+
- Add support for Phonak Target Media
- Add support for Phonak Target Sounds
- Add support for Sonic ExpressFit v2024+
- Add support for Starkey Pro Fit
- Add support for Starkey Inspire
- Fix Starkey intermediate SSL Certificate error
- Fix bugs
- Add exit script
- Pausing after requirement-checks
- Update README

### v1.8.0
- Add native Linux and MacOS Support

### v1.7.6
- Fix debug logging utility bug

### v1.7.5
- Add debug logging utility

### v1.7.4
- Fixed Widex Compass GPS Localisation Errors
- Fixed Typos

### v1.7.3
- Fix bugs

### v1.7.2
- Fix library bug

### v1.7.1
- Fix typos

### v1.7.0
- Add folder selection GUI
- Add support for GN Resound Smart Fit
- Add support for GN Resound Aventa
- Add catch for server index download errors
- Fix download location bugs in Bernafon Oasis & Oticon Genie 2 checkers

### v1.6.3
- Fix folder path selection bug

### v1.6.2
- Fix Unitron checker Bug

### v1.6.1
- Fix Phonak Target checker Bug
- Fix script name mistake

### v1.6.0
- Add support for Rexton Connexx

### v1.5.0
- Add support for OasisNXT
- Fix bugs

### v1.4.0
- Split up the Genie checkers into separate versions
- Update Genie 2 checker to also use updater
- Fix bugs

### v1.3.0
- Add support for Widex Compass GPS

### v1.2.0
- Add support for Unitron TrueFit
- Add downloading progress bar
- Reduce RAM usage when running the script

### v1.1.2
- Fix bugs with selecting download version

### v1.1.0
- Add support for Oticon Genie & Oticon Genie 2

### v1.0.0
- Add support for Phonak Target & Signia Connexx
- Release it publically


## Copyright & DMCA
Since these scripts download data which is publically available online directly from software servers, it does not directly distribute any copyrighted content. If you are a company and are still unhappy with the way one of these scripts works, please open an issue describing how exactly the script violates your software's copyright and it will be modified immediately. (I am not a lawyer, this is not legal advice, this is merely my opinion.)

## WARANTY/SUPPORT
THE SOFTWARE PROVIDED BY THIS SCRIPT IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

THIS SCRIPT UNOFFICIAL AND IS NOT IN ANY AFFILIATED WITH THE AUTHORS OR COPYRIGHT HOLDERS OF ANY SOFTWARE DOWNLOADED VIA THE USE OF THIS SCRIPT. THEY HAVE NO REQUIREMENT TO PROVIDE ANY SUPPORT OR WARANTY TO ANY SOFTWARE DOWNLOADED VIA THE USE OF THIS SCRIPT. THE AUTHORS AND COPYRIGHT HOLDERS OF ANY SOFTWARE DOWNLOADED VIA THE USE OF THIS SCRIPT RESERVE THE RIGHT TO TERMINATE ANY USAGE OF SOFTWARE DOWNLOADED VIA THIS SCRIPT.

## DISCLAIMER
Bluebotlabz and any contributor of these scripts do not take any responsability for what you do using this software. All rights and credit go to their rightful owners. No copyright infringement intended.

Bluebotlabz, any contributor of these scripts, and these checkers are not affiliated with or endorsed by any of the companies mentioned in this repository. Depending on how this software is used, it may violate the EULA and/or Terms and Conditions of the downloaded software. This is an UNOFFICIAL downloader and use of the software downloaded using it may be limited. (I am not a lawyer, this is not legal advice, this is merely my opinion.)

## Appendix
Some less common hearing aid brands can be checked via their official websites:
- Audina [ezFIT](https://www.audina.net/en/professional/software)
- AUSTAR [Fit](https://www.austar-hearing.net/Fitting+Software) and older software can be found [here](https://www.austar-hearing.com/soft-40.html) or [here](https://soft.austar-hearing.com:4431/software-center/#/)
- NewSound [Fit](https://www.newsound.cn/软件下载)
- Persona Medical [ProFit](https://personamedical.com/downloads/)

Note: these software WON'T be included in the checker scripts.
